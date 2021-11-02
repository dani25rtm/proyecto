from flask import Flask
from flask import render_template
import folium

mapa = folium.Map(location=[18.46919296891215, -69.95198616227927],zoom_start=14,)
folium.Marker([18.483702, -69.980505]).add_to(mapa)
folium.Marker([18.484882, -69.998401]).add_to(mapa)
folium.Marker([18.455015, -69.971418]).add_to(mapa)
folium.Marker([18.465410, -69.958769]).add_to(mapa)

#mapa.save('templates\kfc.html')
#mapa.save('templates\pizza.html')
#mapa.save('templates\subway.html')



app = Flask(__name__)


@app.route("/")
def home():
    return render_template('mac.html')


@app.route('/KFC')
def kfc():
    return render_template('kfc.html')


@app.route('/pizza')
def pizza():
    return render_template('pizza.html')


@app.route("/subway")
def subway():
    return render_template('subway.html')



if __name__ == "__main__":
    app.run(debug=True)
