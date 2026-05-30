def test_telegram_service_reachable(driver, config):
    driver.get(f"{config['base_url']}/api/webhook/telegram")
    assert "ERR_" not in driver.page_source, "El webhook de Telegram no es alcanzable"
