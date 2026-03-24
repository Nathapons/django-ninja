from django.shortcuts import render
from ninja import Router

from .user import user_router


router = Router()

router.add_router('/', user_router)