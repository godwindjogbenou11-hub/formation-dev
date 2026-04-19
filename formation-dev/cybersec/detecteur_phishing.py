import re

def analyser_url(url):
    score = 0
    alertes = []

    if re.search(r'[0-9]', url.split('.')[0]):
        score += 2
        alertes.append("⚠️ Chiffres suspects dans le domaine")

    if len(url) > 75:
        score += 1
        alertes.append("⚠️ URL anormalement longue")

    mots_suspects = ['login', 'verify', 'secure', 'account', 'update', 'free', 'win']
    for mot in mots_suspects:
        if mot in url.lower():
            score += 1
            alertes.append(f"⚠️ Mot suspect détecté : {mot}")

    print(f"\n🔍 Analyse de : {url}")
    print(f"Score de risque : {score}/10")
    for alerte in alertes:
        print(alerte)

    if score >= 3:
        print("🔴 DANGER : URL probablement malveillante !")
    elif score >= 1:
        print("🟡 ATTENTION : URL suspecte")
    else:
        print("🟢 URL semble sûre")

analyser_url("http://paypa1-secure-login-verify.com/account")
analyser_url("https://google.com")
