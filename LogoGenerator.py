import svgwrite
import argparse
import string
import os

def pattern(name, logoText):
    dwg = svgwrite.Drawing(name, size=('20cm', '10cm'), profile='full', debug=True)

    #We use dwg.g to use different style fonts, this can be done using the css classes
    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'Fonts.css')
    # set user coordinate space
    dwg.viewbox(width=200, height=150)
    dwg.add_stylesheet(filename, title="sometext") # same rules as for html files
    g = dwg.g(class_="myclass")
    g.add(dwg.text(logoText, insert=(10,30)))
    dwg.add(g)

    pattern = dwg.defs.add(dwg.pattern(size=(20, 20), patternUnits="userSpaceOnUse"))

    #We want to find icons that are of a similar meaning to Bail Bonds... handcuffs, jail, freedom.


    #We want to generate logos with different font styles using google font apis

    pattern.add(dwg.circle((10, 10), 5))
    dwg.add(dwg.circle((100, 100), 50, fill=pattern.get_paint_server()))
    dwg.add(dwg.text(logoText,None, [40], [50]))
    dwg.save()

#if we want this to be a genetic algorithm, how would we define a fitness function?
    #Well it wouldnt really apply to font style choice, but it might apply to location of text and logo

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('CompanyName', type=str)
    args = parser.parse_args()
    CompanyName = args.CompanyName
    pattern("pattern.svg", CompanyName)
