import asyncio

from fastapi import APIRouter
from lnbits.db import Database
from lnbits.tasks import create_permanent_unique_task
from loguru import logger

from .tasks import wait_for_paid_invoices
from .views import paybutton_ext_generic
from .views_api import paybutton_ext_api

db = Database("ext_paybutton")

scheduled_tasks: list[asyncio.Task] = []

paybutton_ext: APIRouter = APIRouter(prefix="/paybutton", tags=["paybutton"])
paybutton_ext.include_router(paybutton_ext_generic)
paybutton_ext.include_router(paybutton_ext_api)

paybutton_static_files = [
    {
        "path": "/paybutton/static",
        "name": "paybutton_static",
    }
]


def paybutton_stop():
    for task in scheduled_tasks:
        try:
            task.cancel()
        except Exception as ex:
            logger.warning(ex)


def paybutton_start():
    # ignore will be removed in lnbits `0.12.6`
    # https://github.com/lnbits/lnbits/pull/2417
    task = create_permanent_unique_task("ext_testing", wait_for_paid_invoices)  # type: ignore
    scheduled_tasks.append(task)
