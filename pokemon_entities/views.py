import folium

from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils.timezone import localtime

from pokemon_entities.models import Pokemon
from pokemon_entities.models import PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def check_active(pokemon_cords):
    appeared_at = pokemon_cords.appeared_at
    disappeared_at = pokemon_cords.disappeared_at
    now = localtime()
    return appeared_at < now < disappeared_at


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = Pokemon.objects.all()
    pokemons_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for cords in pokemons_entities:
        if not check_active(cords):
            continue

        image_url = request.build_absolute_uri(cords.pokemon.image.url)

        add_pokemon(
            folium_map,
            cords.lat,
            cords.lon,
            image_url
        )

    pokemons_on_page = []
    for pokemon in pokemons:
        if pokemon.image:
            image_url = request.build_absolute_uri(pokemon.image.url)
        else:
            image_url = None

        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })




def show_pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, id=pokemon_id)

    requested_pokemon = {
        'id': pokemon.id,
        'title': pokemon.title,
        'title_en': pokemon.title_en,
        'title_jp': pokemon.title_jp,
        'img_url': request.build_absolute_uri(pokemon.image.url),
        'entities': [{'lat': entity.lat, 'lon': entity.lon} for entity in pokemon.entities.all() if check_active(entity)],
        'description': pokemon.description,
    }


    if pokemon.previous_evolution:
        requested_pokemon['previous_evolution']={
            'title_ru': pokemon.previous_evolution.title,
            'pokemon_id': pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(pokemon.previous_evolution.image.url)
        }

    if pokemon.evolutions.all():
        next_generation = pokemon.evolutions.get()
        requested_pokemon['next_evolution']={
            'title_ru': next_generation.title,
            'pokemon_id': next_generation.id,
            'img_url': request.build_absolute_uri(next_generation.image.url)
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in requested_pokemon['entities']:
        add_pokemon(
            folium_map,
            pokemon_entity['lat'],
            pokemon_entity['lon'],
            requested_pokemon['img_url']
        )

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': requested_pokemon
    })
