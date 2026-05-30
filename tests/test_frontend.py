def test_frontend_loads(driver, config):
    driver.get(config["base_url"])
    assert driver.title != "", "El frontend no cargó — el título de la página está vacío"
