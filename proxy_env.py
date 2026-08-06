# =====================================================================
# Запуск Chromium через корпоративный / агентский HTTPS-прокси.
#
# Если задан HTTPS_PROXY (среда с egress-прокси, который перетерминирует
# TLS), Chromium нужно: 1) направить на прокси, 2) ограничить TLS 1.2 —
# handshake TLS 1.3 такой прокси сбрасывает (ERR_CONNECTION_RESET),
# 3) не спотыкаться на самоподписанном сертификате прокси.
#
# Вне такой среды (HTTPS_PROXY не задан) возвращает пустые настройки —
# скрипты работают напрямую, как раньше.
# =====================================================================
import os


def pw_launch_args():
    """Доп. аргументы Chromium и параметры контекста для работы за прокси.

    Возвращает (args: list[str], context_kwargs: dict).
    """
    proxy = os.environ.get("HTTPS_PROXY") or os.environ.get("https_proxy")
    if not proxy:
        return [], {}
    return (
        ["--no-sandbox", f"--proxy-server={proxy}", "--ssl-version-max=tls1.2"],
        {"ignore_https_errors": True},
    )
