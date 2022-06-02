from django.db import models

class Topico(models.Model):
    """Um assunto sobre o qual o usuário está aprendendo."""
    texto = models.CharField(max_length=200)
    # Faz o input da data corrente
    data = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em String do modelo."""
        return self.texto        

class Assuntos(models.Model):
    """Algo específico aprendido sobre um assunto."""
    topico = models.ForeignKey(Topico, on_delete=models.CASCADE)        
    assunto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'assunto'
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.assunto[:50] + "..."
            