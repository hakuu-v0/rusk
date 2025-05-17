class HTMLElement:
    def __init__(self, tag):
        self.tag = tag
        self.children = []

    def add_div(self):
        div = HTMLElement("div")
        self.children.append(div)
        return div

    def render(self):
        inner_html = "".join(child.render() for child in self.children)
        return f"<{self.tag}>{inner_html}</{self.tag}>"


html = HTMLElement("html")
html.add_div()
html.add_div()

print(html.render())
