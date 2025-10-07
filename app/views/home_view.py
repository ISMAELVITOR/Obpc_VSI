from django.views.generic import TemplateView
from django.utils import timezone
from datetime import datetime, timedelta
from app.models.escala import Escala
from app.models.evento import Evento
from app.views.base_view import ProtectedView

class HomeView(ProtectedView, TemplateView):
    template_name = "home.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        # Data atual e do final do mês
        hoje = timezone.now().date()
        final_mes = hoje.replace(day=28) + timedelta(days=4)
        final_mes = final_mes.replace(day=1) - timedelta(days=1)
        
        # Buscar escalas do usuário logado
        escalas_usuario = Escala.objects.filter(pessoa=user).select_related(
            'evento', 'funcao'
        )
        
        # Próximos eventos (a partir de hoje)
        proximos_eventos = escalas_usuario.filter(
            evento__data_inicio__gte=hoje
        ).order_by('evento__data_inicio')[:10]
        
        # Eventos deste mês
        eventos_mes = escalas_usuario.filter(
            evento__data_inicio__range=[hoje, final_mes]
        )
        
        # Total de escalas (todas)
        total_escalas = escalas_usuario.count()
        
        # Preparar dados para o template
        eventos_data = []
        for escala in proximos_eventos:
            eventos_data.append({
                'id': escala.id,
                'nome': escala.evento.nome,
                'data_inicio': escala.evento.data_inicio,
                'hora_inicio': escala.evento.hora_inicio,
                'hora_fim': escala.evento.hora_fim,
                'funcao': escala.funcao.nome,
                'tipo': self._get_tipo_evento(escala.evento.nome),
            })
        
        context.update({
            'proximos_eventos_count': proximos_eventos.count(),
            'eventos_mes_count': eventos_mes.count(),
            'total_escalas_count': total_escalas,
            'eventos': eventos_data,
            'hoje': hoje,
        })
        
        return context
    
    def _get_tipo_evento(self, nome_evento):
        """Determina o tipo do evento baseado no nome"""
        nome_lower = nome_evento.lower()
        if 'culto' in nome_lower:
            return 'culto'
        elif 'ensaio' in nome_lower:
            return 'ensaio'
        elif 'jovem' in nome_lower or 'juventude' in nome_lower:
            return 'jovens'
        else:
            return 'especial'
