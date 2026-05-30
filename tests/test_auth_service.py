def test_auth_health(driver, config):
    driver.get(f"{config['base_url']}/api/v1/auth/health")
    assert "ERR_" not in driver.page_source, "El servicio de autenticación no es alcanzable"
