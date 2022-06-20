def test_docker_is_installed(host):
    # testen, ob das Paket "docker-ce" installiert ist
    assert host.package("docker-ce").is_installed

def test_docker_service_is_running(host):
    # testen, ob der Service "docker" läuft und verfügbar ist
    assert host.service("docker").is_running

def test_heroapp_container_is_running(host):
    # testen, ob der container mit dem Namen "my-hero-app" läuft
    assert host.docker("my-hero-app").is_running

def test_heroapp_is_available_on_port_80(host):
    # testen, ob auf tcp://0.0.0.0:80 gehorcht wird
    assert host.socket("tcp://0.0.0.0:80").is_listening
