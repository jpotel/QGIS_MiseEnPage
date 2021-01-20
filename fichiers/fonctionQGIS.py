from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def dimension_objet_mise_en_page(value1, value2, value3, feature, parent):
    """
    Donne la hauteur ou la largeur d'un objet d'une mise en page.
    <h2>Example usage:</h2>
    <ul>
      <li>dimension_objet_mise_en_page('mise_en_page','objet','hauteur') -> 13</li>
      <li>dimension_objet_mise_en_page('mise_en_page','objet','largeur') -> 12</li>
    </ul>
    """
    manager = QgsProject.instance().layoutManager()
    layout = manager.layoutByName(value1)
    mapItem = layout.itemById(value2)
    if value3 == "hauteur":
       return mapItem.rectWithFrame().height()
    elif value3 == "largeur":
        return mapItem.rectWithFrame().width()
    else:
        return "erreur"