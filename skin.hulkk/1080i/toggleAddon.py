import json
import xbmc

################################################################################
################################################################################
#####             Enable Disable Addons       Code by Quihico              #####
################################################################################
################################################################################

def dis_or_enable_addon(addon_id, enable="true"):
    addon = '"%s"' % addon_id
    if xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "true":
        return print("### Skipped %s, reason = allready enabled" % addon_id)
    elif not xbmc.getCondVisibility("System.HasAddon(%s)" % addon_id) and enable == "false":
        return print("### Skipped %s, reason = not installed" % addon_id)
    else:
        do_json = '{"jsonrpc":"2.0","id":1,"method":"Addons.SetAddonEnabled","params":{"addonid":%s,"enabled":%s}}' % (addon, enable)
        query = xbmc.executeJSONRPC(do_json)
        response = json.loads(query)
        if enable == "true":
            print("### Enabled %s, response = %s" % (addon_id, response))
        else:
            print("### Disabled %s, response = %s" % (addon_id, response))
    # return xbmc.executebuiltin('Container.Update(%s)' % xbmc.getInfoLabel('Container.FolderPath'))


################################################################################
################################################################################
#####        Toggle Enable Disable Addons       Code by OptimusGREEN       #####
################################################################################
################################################################################


def toggleEnabled(addon_id):
    import json, xbmc
    getState = xbmc.executeJSONRPC('{"jsonrpc": "2.0", "method": "Addons.GetAddonDetails", "params": {"addonid": "%s","properties":["enabled","name"]}, "id": 1}' % (addon_id))
    response = json.loads(getState)
    result = response.get("result")
    addonDict = result.get("addon")
    isEnabled = addonDict.get("enabled")
    if isEnabled:
        dis_or_enable_addon(addon_id, enable="false")
    if not isEnabled:
        dis_or_enable_addon(addon_id, enable="true")




# PUT YOUR ADDON ID IN THE INVERTED COMMAS BELOW. THEN TRIGGER WITH : RunScript("full path to this py file")
myAddon = "pvr.stalker"
toggleEnabled(myAddon)
