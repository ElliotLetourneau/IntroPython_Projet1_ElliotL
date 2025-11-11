import requests


URL = "https://pax.ulaval.ca/quoridor/api/a25/"

#________________________________________créer_une_partie________________________________________

def créer_une_partie(idul, secret):
    rep = requests.post(f"{URL}/jeux", auth=(idul, secret))

    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["état"]

    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])

    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])

    else:
        raise ConnectionError

#________________________________________appliquer_un_coup________________________________________

def appliquer_un_coup(id_partie, coup, position, idul, secret):
    rep = requests.put(
        f"{URL}/jeux/{id_partie}",
        auth=(idul, secret),
        json={"coup": coup, "position": position},
    )

    if rep.status_code == 200:
        data = rep.json()
        if data["partie"] == "terminée":
            raise StopIteration(data["gagnant"])
        return data["coup"], data["position"]

    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])

    elif rep.status_code == 404:
        raise ReferenceError(rep.json()["message"])

    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])

    else:
        raise ConnectionError

#________________________________________récupérer_une_partie________________________________________

def récupérer_une_partie(id_partie, idul, secret):
    rep = requests.get(f"{URL}/jeux/{id_partie}", auth=(idul, secret))

    if rep.status_code == 200:
        data = rep.json()
        return data["id"], data["état"]

    elif rep.status_code == 401:
        raise PermissionError(rep.json()["message"])

    elif rep.status_code == 404:
        raise ReferenceError(rep.json()["message"])

    elif rep.status_code == 406:
        raise RuntimeError(rep.json()["message"])

    else:
        raise ConnectionError