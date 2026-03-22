from app.services.ai.factory import get_ai_provider


class ClassifyEmailUseCase:

    def __init__(self):
        self.ai_provider = get_ai_provider()

    def execute(self, content: str):
        prompt = f"""
        Classifique o seguinte email como produtivo ou improdutivo
        e gere uma resposta apropriada.

        Email:
        {content}

        Responda no formato JSON:
        {{
            "category": "produtivo ou improdutivo",
            "suggested_response": "resposta aqui"
        }}
        """

        response = self.ai_provider.generate(prompt)

        return response