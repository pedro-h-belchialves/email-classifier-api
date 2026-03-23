from fastapi import APIRouter, HTTPException
from app.schemas.email_schema import EmailRequest, EmailResponse
from app.services.use_cases import ClassifyEmailUseCase

router = APIRouter()

@router.post("/classify", response_model=EmailResponse)
def classify_email(request: EmailRequest):
    try:
        use_case = ClassifyEmailUseCase()

        result = use_case.execute(request.content)

        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao processar email: {str(e)}"
        )