# constantes_texto.py

URL_LOGIN_OGAME = "https://lobby.ogame.gameforge.com/es_AR/accounts"

# Rutas para el menú de login
LOGIN_TAB_SELECTOR = "#loginRegisterTabs > ul > li:nth-child(1)"
EMAIL_INPUT_SELECTOR = "#loginForm > div:nth-child(2) > div > input[type=email]"
PASSWORD_INPUT_SELECTOR = "#loginForm > div:nth-child(3) > div > input[type=password]"
LOGIN_BUTTON_SELECTOR = "#loginForm > p > button.button.button-primary.button-lg"
LOGIN_BUTTON_JOIN_GAME_SELECTOR = "#joinGame > a > button"
LOGIN_BUTTON_JOIN_THE_SERVER_SELECTOR = "#accountlist > div > div.rt-table > div.rt-tbody > div > div > div.rt-td.action-cell > button"


# Rutas menus 
#Menu Recursos
TAB_RECURSOS_SELECTOR = "#menuTable > li:nth-child(2) > a"

# Rutas para los recursos en tiempo real.
METAL_SELECTOR = "#resources_metal"                
CRISTAL_SELECTOR = "#resources_crystal"
DEUTERIO_SELECTOR = "#resources_deuterium"
ENERGIA_SELECTOR = "#resources_energy"

# Rutas Mina de metal
CURRENT_LEVEL_MINE_METAL_SELECTOR = "#producers > li.technology.metalMine.hasDetails.tooltip.hideTooltipOnMouseenter.js_hideTipOnMobile.ipiHintable > span > span > span.stockAmount"
BUTTON_MINE_METAL_SELECTOR = "#producers > li.technology.metalMine.hasDetails.tooltip.hideTooltipOnMouseenter.js_hideTipOnMobile.ipiHintable > span"
METAL_COST_SELECTOR = "#technologydetails > div.content > div > div.costs > ul > li.resource.metal.icon.insufficient.tooltip.js_hideTipOnMobile"
CRISTAL_COST_SELECTOR = "#technologydetails > div.content > div > div.costs > ul > li.resource.crystal.icon.sufficient.tooltip.js_hideTipOnMobile"
ENERGY_COST_SELECTOR = "#technologydetails > div.content > div > ul > li.additional_energy_consumption > span"
