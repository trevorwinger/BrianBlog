class PostInformation:
    def __init__(self, number, content):
        self.n = number
        self.c = content
    
    def make_post(self):
        if self.n == 1:
            return '<h1>' + self.c + '</h1>'
        elif self.n == 2:
            return '<p>' + self.c + '</p>'
        elif self.n == 3:
            return '<span class="image fit">' + '<img src='+ self.c +'alt=""/></span>'
        elif self.n == 4:
            return '<iframe height=1000 width="100%" src=' + self.c + 'frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>'
        elif self.n == 5:
            return ''
        else:
            return ''


def main():
    title = input("Title: ")
    blog_body = input("Blog contents: ")
    generate_blog(title, blog_body)

def generate_blog(title, body):
    filename = 'auto_gen.html'
    message = """<!DOCTYPE HTML>
        <html>
	        <head>
		        <title>Red, White & Blue</title>
		        <meta charset="utf-8" />
		        <meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no" />
		        <link rel="stylesheet" href="assets/css/main.css" />
		        <noscript><link rel="stylesheet" href="assets/css/noscript.css" /></noscript>
	        </head>
	        <body class="is-preload">

		        <!-- Wrapper -->
			    <div id="wrapper">

				    <!-- Header -->
					    <header id="header" class="alt">
						    <a href="index.html" class="logo"><strong>theredwhite.blue</strong> <span>by Brian Daniel</span></a>
					    </header>

				    <!-- Main -->
					    <div id="main" class="alt">

						    <!-- One -->
							    <section id="one">
								    <div class="inner">
									    <header class="major">
                                            <h1>%s</h1>
                                        </header>
                                        <p>%s</p>
                                    </div>
							    </section>

					    </div>

				    <!-- Footer -->
				    <footer id="footer">
					    <div class="inner">
						    <ul class="icons">
							    <li><a href="soon.html" class="icon brands alt fa-twitter"><span class="label">Twitter</span></a></li>
							    <li><a href="soon.html" class="icon brands alt fa-facebook-f"><span class="label">Facebook</span></a></li>
							    <li><a href="soon.html" class="icon brands alt fa-instagram"><span class="label">Instagram</span></a></li>
							    <li><a href="soon.html" class="icon brands alt fa-youtube"><span class="label">YouTube</span></a></li>
							    <li><a href="soon.html" class="icon brands alt fa-soundcloud"><span class="label">Sound Cloud</span></a></li>
						    </ul>
					    </div>
				    </footer>

			    </div>

		        <!-- Scripts -->
			        <script src="assets/js/jquery.min.js"></script>
			        <script src="assets/js/jquery.scrolly.min.js"></script>
			        <script src="assets/js/jquery.scrollex.min.js"></script>
			        <script src="assets/js/browser.min.js"></script>
			        <script src="assets/js/breakpoints.min.js"></script>
			        <script src="assets/js/util.js"></script>
			        <script src="assets/js/main.js"></script>

	        </body>
        </html>"""
    with open(filename, 'w') as f:
        whole = message % (title, body)
        f.write(whole)
        f.close()


main()