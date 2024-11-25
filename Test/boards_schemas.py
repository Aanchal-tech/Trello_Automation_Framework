from voluptuous import Schema, Required, All, Any, Length, Object, Optional

# {"name":"morpheus","job":"leader","id":"417","createdAt":"2021-10-20T07:27:17.815Z"}
class Schemas:

    def __init__(self):

        self.create_emp_record_201 = Schema(Object(
            {
            Required('http_code'):201,
            Required('name'): All(str),
            Required('job'): All(str),
            Required('id'): All(str),
            Required('createdAt'): All(str),
            # Required('createdAt'): Any(None, str, int, list),
        }))
        self.create_emp_record_201_new = Schema(
            {
                # Required('http_code'): 201,
                Required('name'): All(str),
                Required('job'): All(str),
                Required('id'): All(str),
                Required('createdAt'): All(str),
                # Required('createdAt'): Any(None, str, int, list),
            })


        self.creat_board_201 = Schema(

            {
                Required("id"): All(str),
                Required("name"): All(str),
                Required("desc"): All(str),
                Required("descData"): Any(None, str),
                Required("closed"): Any(bool),
                Required("idOrganization"): All(str),
                Required("idEnterprise"): Any(None, str),
                Required("pinned"): Any(bool),
                Required("url"): All(str),
                Required("shortUrl"): All(str),
                Required("prefs"): Schema({
                    Required("permissionLevel") : All(str),
                    Required("hideVotes") : All(bool),
                    Required("voting") : All(str),
                    Required("comments") : All(str),
                    Required("invitations") : All(str),
                    Required("selfJoin") : All(bool),
                    Required("cardCovers") : All(bool),
                    Required("isTemplate") : All(bool),
                    Required("cardAging") : All(str),
                    Required("calendarFeedEnabled"): All(bool),
                    Required("isPluginHeaderShortcutsEnabled") : All(bool),
                    Required("enabledPluginBoardButtons") : All(list),
                    Required("background") : All(str),
                    Required("backgroundImage") : Any(None, str),
                    Required("backgroundImageScaled") : Any(None, str),
                    Required("backgroundTile") : All(bool),
                    Required("backgroundBrightness") : All(str),
                    Required("backgroundColor"): All(str),
                    Required("backgroundBottomColor"): All(str),
                    Required("backgroundTopColor") : All(str),
                    Required("canBePublic") : All(bool),
                    Required("canBeEnterprise") : All(bool),
                    Required("canBeOrg") : All(bool),
                    Required("canBePrivate") : All(bool),
                    Required("canInvite") : All(bool)
                }),
                Required("labelNames") : Schema({
                    Required("green") : Any(None, str),
                    Required("yellow") : Any(None, str),
                    Required("orange") : Any(None, str),
                    Required("red") : Any(None, str),
                    Required("purple") : Any(None, str),
                    Required("blue") : Any(None, str),
                    Required("sky") : Any(None, str),
                    Required("lime") : Any(None, str),
                    Required("pink") : Any(None, str),
                    Required("black") : Any(None, str)
                }),
                Required("limits") : dict

                }



        )

        self.update_board_200 = Schema(

                {
                    Required("id"): All(str),
                    Required("name"):All(str),
                    Required("desc"): All(str),
                    Required("descData"): Any(None, str),
                    Required("closed"): Any(bool),
                    Required("idOrganization"): All(str),
                    Required("idEnterprise"): Any(None,str),
                    Required("pinned"): Any(bool),
                    Required("url"): All(str),
                    Required("shortUrl"): All(str),
                    Required("prefs"): Schema({
                        Required("permissionLevel"): All(str),
                        Required("hideVotes"): All(bool),
                        Required("voting"): All(str),
                        Required("comments"): All(str),
                        Required("invitations"): All(str),
                        Required("selfJoin"): All(bool),
                        Required("cardCovers"): All(bool),
                        Required("isTemplate"): All(bool),
                        Required("cardAging"): All(str),
                        Required("calendarFeedEnabled"): All(bool),
                        Required("isPluginHeaderShortcutsEnabled"): All(bool),
                        Required("enabledPluginBoardButtons"): All(list),
                        Required("background"): All(str),
                        Required("backgroundImage"): Any(None,str),
                        Required("backgroundImageScaled"): Any(None,str),
                        Required("backgroundTile"): All(bool),
                        Required("backgroundBrightness"): All(str),
                        Required("backgroundColor"): All(str),
                        Required("backgroundBottomColor"): All(str),
                        Required("backgroundTopColor"): All(str),
                        Required("canBePublic"): All(bool),
                        Required("canBeEnterprise"): All(bool),
                        Required("canBeOrg"): All(bool),
                        Required("canBePrivate"): All(bool),
                        Required("canInvite"): All(bool)
                    }),
                    Required("labelNames"): ({
                        Required("green"):  Any(None, str),
                        Required("yellow"):  Any(None, str),
                        Required("orange"):  Any(None, str),
                        Required("red"):  Any(None, str),
                        Required("purple"):  Any(None, str),
                        Required("blue"):  Any(None, str),
                        Required("sky"):  Any(None, str),
                        Required("lime"):  Any(None, str),
                        Required("pink"):  Any(None, str),
                        Required("black"):  Any(None, str)
                    }),
                }

        )

