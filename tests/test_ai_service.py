def test_ai_health(driver, config):
    driver.get(f"{config['base_url']}/api/ai/healthh")
    assert "ERR_" not in driver.page_source, "El servicio de IA no es alcanzable"
