# Import Packages
from fastapi import FastAPI


# App Instance
AM = FastAPI()


# ============================================================
# * API Router
# ============================================================

# * Asset Management

from app.internal.logistics.am.routes.asset_management import asset_route, asset_type_route, asset_provider_route, maintenance_provider_route, maintenance_route, event_route
from app.internal.logistics.am.routes.asset_management import missing_asset_route, asset_request_route, sell_asset_route, dispose_asset_route, broken_asset_route, repair_asset_route
from app.internal.logistics.am.routes.asset_management import maintenance_report_route, check_out_route, check_in_route, asset_warranty_route
    
AM.include_router(asset_route.router)
AM.include_router(asset_type_route.router)
AM.include_router(asset_provider_route.router)
AM.include_router(maintenance_provider_route.router)
AM.include_router(maintenance_route.router)
AM.include_router(event_route.router)
AM.include_router(missing_asset_route.router)
AM.include_router(asset_request_route.router)
AM.include_router(sell_asset_route.router)
AM.include_router(dispose_asset_route.router)
AM.include_router(broken_asset_route.router)
AM.include_router(repair_asset_route.router)
AM.include_router(maintenance_report_route.router)
AM.include_router(check_out_route.router)
AM.include_router(check_in_route.router)
AM.include_router(asset_warranty_route.router)


# ============================================================
# * Web Routers
# ============================================================

# * Human Resource
# ? Recruitment
from app.internal.human_resource.rms.routers.web \
    import redirect_webRouter, deptHead_webRoute, deptMngr_webRoute, hireMngr_webRoute, recruiter_webRoute
RMS.include_router(redirect_webRouter.router)
RMS.include_router(deptHead_webRoute.router)
RMS.include_router(deptMngr_webRoute.router)
RMS.include_router(hireMngr_webRoute.router)
RMS.include_router(recruiter_webRoute.router)