def givePriv(role):
    if role.lower() == "reader":
        API.displayReaderView()
    if role.lower() == "contributer":
        API.displayReaderView()
    if role.lower() == "desk editor":
        API.displayDeskEdiView()
    if role.lower() == "desk head":
        API.displayDeskHeadView()
    if role.lower() == "copy editor":
        API.displayCopyEdiView()
    if role.lower() = "assistant copy chief":
        API.displayAssisCopyChiefView()
    if role.lower() = "copy chief":
        API.displayCopyChiefView()
    if role.lower() = "editor in chief":
        API.displayEditorInChiefView()
