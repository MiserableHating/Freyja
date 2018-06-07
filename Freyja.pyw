import admin
import os

if not admin.isUserAdmin():
        admin.runAsAdmin()
