MDFloatLayout:
    size_hint_x: None
    size_hint_y: None
    size: (dp(110), dp(100))
    # pos_hint: {"center_x": .3, "center_y":.7}
    adaptive_height: True
    canvas:
        Color:
            # rgba: gch(root.auc_color)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(3),]
