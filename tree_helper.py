from PySide6.QtWidgets import QTreeWidgetItem, QSpacerItem, QSizePolicy
from PySide6.QtCore import Qt, QTimer
import color_helper

def set_up_trees(window):
    clear_all(window)
    for tree in window.trees:
        tree.itemSelectionChanged.connect(lambda t=tree: handle_selection_changed(window, t))

        # Disable internal scrolling on your tree
        tree.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        tree.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Use a lambda to pass your tree instance into the standalone function
        tree.expanded.connect(lambda _, t=tree: adjust_tree_height(t))
        tree.collapsed.connect(lambda _, t=tree: adjust_tree_height(t))

        tree.itemCollapsed.connect(lambda item, t=tree: prevent_selected_parent_collapse(window, t))

    if window.trees:
        parent_layout = window.trees[0].parentWidget().layout()
        if parent_layout:
            # Create a vertical expanding spacer push-rod
            spacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
            parent_layout.addItem(spacer)

def clear_mess_dependent(window):
    for elem in window.can_lock:
        elem.setDisabled(True)
        elem.blockSignals(True)

    window.selected_message = None
    window.ui.newText.setText("")
    window.ui.origText.setText("")
    window.ui.selected_expr.setValue(0)
    window.ui.expr_width.setValue(0)
    window.ui.expr_height.setValue(0)
    window.ui.expr_hp.setValue(0)
    window.ui.expr_vp.setValue(0)
    color = "#00000000"
    color_helper.set_color(window, "outline", window.ui.expr_outline, color)
    color_helper.set_color(window, "color", window.ui.expr_color, color)
    window.ui.start_expr.setCurrentIndex(0)
    window.ui.middle_expr.setCurrentIndex(0)
    window.ui.end_expr.setCurrentIndex(0)
    window.ui.gameView.setText("")
    window.ui.gameView.setPixmap(None)

    for elem in window.can_lock:
        elem.blockSignals(False)

def clear_all(window):
    for tree in window.trees:
        tree.clear()
        tree.children = {}
        tree.setMaximumSize(16777215, 16777215)
        tree.setMinimumSize(0, 0)
    window.unsaved_changes = False
    adjust_tree_height(window.ui.searched)
    clear_mess_dependent(window)

    window.setWindowTitle("Wii Party Text Editor")
    window.ui.num_expressions.setText("")

def add_to_tree(window, msg, selTree, i):
    if msg.type not in selTree.children:
        new_entry = QTreeWidgetItem(selTree, [msg.type])
        parent_flags = new_entry.flags()
        new_entry.setFlags(parent_flags & ~Qt.ItemFlag.ItemIsSelectable)
        new_entry.children = []
        selTree.children[msg.type] = new_entry

    child_item = QTreeWidgetItem(selTree.children[msg.type], [msg.name])
    child_item.id = i
    selTree.children[msg.type].children.append(child_item)

def populate_xmsg(window):
    clear_all(window)
    for i in range(window.deser.num_messages):
        msg = window.deser.messages[i]
        selTree = matchTypeToTree(window, msg.name)
        add_to_tree(window, msg, selTree, i)
    for tree in window.trees:
        QTimer.singleShot(0, lambda t=tree: adjust_tree_height(t))
    window.ui.num_expressions.setText("of " + str(len(window.deser.expressions) - 1))
    window.ui.selected_expr.setMaximum(len(window.deser.expressions) - 1)

def populate_search_tree(window, query):
    query = query.lower().replace("\n", "")
    search_style = -1
    if("style:" in query):
        style = query.find("style:")
        styleEnd = query.find(" ", style)
        if(styleEnd == -1):
            styleEnd = len(query)
        search_style = int(query[style:styleEnd].split(":")[1])
        query = (query[:style] + query[styleEnd:])
    query = query.replace(" ", "")

    #clear current search tree
    if window.ui.searched.currentItem():
        window.ui.searched.clearSelection()
        clear_mess_dependent(window)

    window.selected_message = None
    window.ui.searched.clear()
    window.ui.searched.children = {}
    window.ui.searched.setMaximumSize(16777215, 16777215)
    window.ui.searched.setMinimumSize(0, 0)

    for i in range(window.deser.num_messages):
        msg = window.deser.messages[i]
        if (
            (
                query in msg.type.lower().replace(" ", "").replace("\n", "")
                or query in msg.text.lower().replace(" ", "").replace("\n", "")
                or query in msg.name.lower().replace(" ", "").replace("\n", "")
            )
            and ((msg.exp_index == search_style) or (search_style == -1))
        ):
            add_to_tree(window, msg, window.ui.searched, i)
    QTimer.singleShot(0, lambda t=window.ui.searched: adjust_tree_height(t))


def prevent_selected_parent_collapse(window, tree_widget):
    # Get the currently selected item in this tree
    selected_item = tree_widget.currentItem()
    tree_widget.clearSelection()

    if not selected_item:
        return

    clear_mess_dependent(window)

def adjust_tree_height(tree_widget):
    # Calculate header height
    tree_widget.executeDelayedItemsLayout()
    total_height = tree_widget.header().height() if not tree_widget.isHeaderHidden() else 0

    # Helper lambda function to recursively calculate item heights
    def get_branch_height(item):
        height = tree_widget.visualItemRect(item).height()
        if item.isExpanded():
            for i in range(item.childCount()):
                height += get_branch_height(item.child(i))
        return height

    # Sum up all visible items
    for i in range(tree_widget.topLevelItemCount()):
        total_height += get_branch_height(tree_widget.topLevelItem(i))

    # Account for widget margins/borders
    padding = (tree_widget.frameWidth() * 2) + 4
    total_height += padding

    # Force the tree widget to update its size
    tree_widget.setFixedHeight(total_height)

def ensure_tree_item_visible(window, sending_tree):
    item_rect = sending_tree.visualItemRect(sending_tree.currentItem())

    # 2. Map that rectangle's position to the global coordinates of the Scroll Area
    # This tells us exactly where the item is relative to the scroll window viewport
    item_global_top = sending_tree.mapTo(window.ui.string_container.widget(), item_rect.topLeft()).y()
    item_global_bottom = item_global_top + item_rect.height()

    # 3. Get the current viewport boundaries of the scroll area
    scrollbar = window.ui.string_container.verticalScrollBar()
    view_top = scrollbar.value()
    view_bottom = view_top + window.ui.string_container.viewport().height()

    # Padding so the item isn't jammed right against the pixel edge of the window
    padding = 20

    # 4. Adjust the scrollbar if the item has gone off-screen
    if item_global_top < view_top + padding:
        # User arrowed UP out of view -> scroll up
        scrollbar.setValue(item_global_top - padding)
    elif item_global_bottom > view_bottom - padding:
        # User arrowed DOWN out of view -> scroll down
        scrollbar.setValue(item_global_bottom - window.ui.string_container.viewport().height() + padding)


def focus_on_selected_node(window):
    # 1. Find which tree actually has an item selected
    active_tree = None
    active_item = None

    for tree in window.trees:
        if tree.selectedItems():
            active_tree = tree
            active_item = tree.currentItem()
            break # Found it, stop scanning

    # 2. If nothing is selected anywhere, do nothing
    if not active_tree or not active_item:
        print("No node is currently selected to focus on.")
        return

    # 3. Reuse your viewport mapping logic to snap the scroll area to the node
    # (Assuming self.ui.scrollArea is your Designer scroll area container)
    ensure_tree_item_visible(window, active_tree)

def handle_selection_changed(window, sending_tree):
        # Identify which tree triggered the signal

        # If the tree that sent the signal has no selection (e.g., it was just cleared),
        # do nothing to avoid unnecessary processing.
        if not sending_tree.selectedItems():
            return

        # Clear selection on all OTHER trees
        for tree in window.trees:
            if tree is not sending_tree:
                # Block signals temporarily so clearing this tree doesn't
                # trigger this function recursively.
                tree.blockSignals(True)
                tree.clearSelection()
                tree.blockSignals(False)

        window.selected_message = sending_tree.currentItem().id

        ensure_tree_item_visible(window, sending_tree)
        for elem in window.can_lock:
            elem.setDisabled(False)
            elem.blockSignals(True)
        window.ui.newText.setText(window.deser.messages[window.selected_message].text)
        window.ui.origText.setText(window.orig_deser.messages[window.selected_message].text)
        update_expressions(window)
        color_helper.render_game_view(window)
        for elem in window.can_lock:
            elem.blockSignals(False)


def update_expressions(window):
    exp_index = window.deser.messages[window.selected_message].exp_index
    window.ui.selected_expr.setValue(exp_index)
    window.ui.expr_width.setValue(window.deser.expressions[exp_index].width)
    window.ui.expr_height.setValue(window.deser.expressions[exp_index].height)
    window.ui.expr_hp.setValue(window.deser.expressions[exp_index].horizontal_spacing)
    window.ui.expr_vp.setValue(window.deser.expressions[exp_index].vertical_spacing)
    window.ui.start_expr.setCurrentIndex(window.deser.expressions[exp_index].states[0])
    window.ui.middle_expr.setCurrentIndex(window.deser.expressions[exp_index].states[1])
    window.ui.end_expr.setCurrentIndex(window.deser.expressions[exp_index].states[2])
    color_helper.set_color(window, "color", window.ui.expr_color, color_helper.hexRgba_to_hexArgb(window.deser.expressions[exp_index].color))
    color_helper.set_color(window, "outline", window.ui.expr_outline, color_helper.hexRgba_to_hexArgb(window.deser.expressions[exp_index].outline))


def matchTypeToTree(window, mess_name):
    def isMinigame(mess_name):
        return (mess_name.startswith("mg") or
            mess_name.startswith("MG") or
            mess_name.startswith("m6"))
    def isPairGame(mess_name):
        return (mess_name.startswith("rank") or
                mess_name.startswith("m062") or
                mess_name.startswith("m041") or
                mess_name.startswith("m05") or
                mess_name.startswith("m08"))
    def isPartyGame(mess_name):
        return ((mess_name.startswith("m0") and not
            mess_name.startswith("m062") and not
            mess_name.startswith("m041") and not
            mess_name.startswith("m05") and not
            mess_name.startswith("m08")) or
            mess_name.startswith("m741"))
    def isHouseGame(mess_name):
        return mess_name.startswith("m7") and not mess_name.startswith("m741")
    def isMenu(mess_name):
        return (mess_name.startswith("pause") or
                mess_name.startswith("retry") or
                mess_name.startswith("conc") or
                mess_name.startswith("mn") or
                mess_name.startswith("top") or
                mess_name.startswith("mr"))
    if isMinigame(mess_name):
        return window.ui.minigames
    elif isPairGame(mess_name):
        return window.ui.pair
    elif isPartyGame(mess_name):
        return window.ui.party
    elif isHouseGame(mess_name):
        return window.ui.house
    elif isMenu(mess_name):
        return window.ui.menu
    return window.ui.system