from fastapi import Depends, Request
from fastapi.templating import Jinja2Templates
from starlette.responses import HTMLResponse

from lnbits.core.models import User
from lnbits.decorators import check_user_exists

from . import paybutton_ext, paybutton_renderer

templates = Jinja2Templates(directory="templates")


@paybutton_ext.get("/", response_class=HTMLResponse)
async def index(
    request: Request,
    user: User = Depends(check_user_exists),
):
    return paybutton_renderer().TemplateResponse(
        "paybutton/index.html", {"request": request, "user": user.dict()}
    )
