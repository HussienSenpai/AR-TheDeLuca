# TODO: Translation updated at 2019-07-29 20:03

translate arabic strings:

    # game/inventory_screen.rpy:86
    old "Head"
    new "رأس"

    # game/inventory_screen.rpy:93
    old "Chest"
    new "صدر"

    # game/inventory_screen.rpy:100
    old "Legs"
    new "رجل"

    # game/inventory_screen.rpy:107
    old "weapon"
    new "سلاح"

    # game/inventory_screen.rpy:115
    old "Body"
    new "جسد"

    # game/inventory_screen.rpy:122
    old "Accessory"
    new "إكسسوارات"

    # game/inventory_screen.rpy:158
    old "Selected Item:"
    new "القطعة المختارة: "

    # game/inventory_screen.rpy:166
    old "{color=#dbb200}[selected_item.nam]{/color}\nAtk: {color=#ffffff}[selected_item.atk]{/color} Def: {color=#ffffff}[selected_item.defense]{/color}\nStealth: {color=#ffffff}[selected_item.stealth]{/color} \nThreat: {color=#ffffff}[selected_item.stealth2]{/color}\n\n{color=#f7f6ef}{u}[selected_item.desc]{/u}{/color} "
    new "{color=#dbb200}[selected_item.nam]{/color}\n{color=#ffffff}[selected_item.atk]{/color} هجوم: {color=#ffffff}[selected_item.defense]{/color} دفاع: \n{color=#ffffff}[selected_item.stealth]{/color} تخفي:  \n{color=#ffffff}[selected_item.stealth2]{/color} تهديد: \n\n{color=#f7f6ef}{u}[selected_item.desc]{/u}{/color} "


    # game/inventory_screen.rpy:174
    old "{b}Unequip{/b}"
    new "{b}إزالة{/b}"

    # game/inventory_screen.rpy:176
    old "{b}Equip{/b}"
    new "{b}إستخدام{/b}"

    # game/inventory_screen.rpy:179
    old "{b}Discard{/b}"
    new "{b}حذف{/b}"

    # game/inventory_screen.rpy:179
    old "Are you sure you want to discard this item?"
    new "هل أنت متأكد من رغبتك بحذف هذه القطعة؟"

    # game/inventory_screen.rpy:255
    old "{color=#dbb200}[selected_shopitem.nam]{/color}\nPrice: ${color=#7bd186}[selected_shopitem.value]{/color}\n\nAtk: {color=#ffffff}[selected_shopitem.atk]{/color} Def: {color=#ffffff}[selected_shopitem.defense]{/color}\nStealth: {color=#ffffff}[selected_shopitem.stealth]{/color} \nThreat: {color=#ffffff}[selected_shopitem.stealth2]{/color}\n\n{color=#f7f6ef}{u}[selected_shopitem.desc]{/u}{/color} "
    new "{color=#dbb200}[selected_shopitem.nam]{/color}\n${color=#7bd186}[selected_shopitem.value]{/color} السعر: \n\n{color=#ffffff}[selected_shopitem.atk]{/color}  هجوم: {color=#ffffff}[selected_shopitem.defense]{/color} دفاع: \n{color=#ffffff}[selected_shopitem.stealth]{/color}  تخفي: \n{color=#ffffff}[selected_shopitem.stealth2]{/color} تهديد: \n\n{color=#f7f6ef}{u}[selected_shopitem.desc]{/u}{/color}"


    # game/inventory_screen.rpy:257
    old "{color=#dbb200}[selected_shopitem.nam]{/color}\nPrice: ${color=#aa0000}[selected_shopitem.value]{/color}\n\nAtk: {color=#ffffff}[selected_shopitem.atk]{/color} Def: {color=#ffffff}[selected_shopitem.defense]{/color}\nStealth: {color=#ffffff}[selected_shopitem.stealth]{/color} \nThreat: {color=#ffffff}[selected_shopitem.stealth2]{/color}\n\n{color=#f7f6ef}{u}[selected_shopitem.desc]{/u}{/color} "
    new "{color=#dbb200}[selected_shopitem.nam]{/color}\n${color=#aa0000}[selected_shopitem.value]{/color} السعر: \n\n{color=#ffffff}[selected_shopitem.atk]{/color}  هجوم: {color=#ffffff}[selected_shopitem.defense]{/color} دفاع: \n{color=#ffffff}[selected_shopitem.stealth]{/color}  تخفي: \n{color=#ffffff}[selected_shopitem.stealth2]{/color} تهديد: \n\n{color=#f7f6ef}{u}[selected_shopitem.desc]{/u}{/color}"

    # game/inventory_screen.rpy:262
    old "{b}Buy{/b}"
    new "{b}شراء{/b}"

    # game/inventory_screen.rpy:262
    old "Purchase the {color=#dbb200}[selected_shopitem.nam]{/color}\nfor $[selected_shopitem.value]?"
    new "{color=#dbb200}[selected_shopitem.nam]{/color} هل ترغب بشار\n$[selected_shopitem.value] مقابل"

    # game/inventory_screen.rpy:264
    old "{b}Can't afford{/b}"
    new "{b}ليس لديك ما يكفي من المال{/b}"

