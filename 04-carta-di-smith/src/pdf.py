from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(); pg=b.new_page(viewport={"width":1280,"height":720})
    pg.goto("file://"+__import__("os").path.abspath("slides.html")+""); pg.wait_for_timeout(300)
    pg.pdf(path="Carta_di_Smith_IV3HGA.pdf",width="1280px",height="720px",print_background=True)
    b.close()
