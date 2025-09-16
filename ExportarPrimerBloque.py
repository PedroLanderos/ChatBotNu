# bot_nu.py
# -*- coding: utf-8 -*-
import re
import unicodedata

def normaliza(txt: str) -> str:
    txt = txt.strip().lower()
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(ch for ch in txt if unicodedata.category(ch) != "Mn")
    return txt

def pedir_no_vacio(prompt: str) -> str:
    while True:
        s = input(prompt)
        if s is None:
            continue
        s = s.strip()
        if s:
            return s
        print("No entendí bien. ¿Puedes escribir tu duda con más detalle?")

salir_RE  = re.compile(r"(?:\b|^)(?:no|salir|me equivoque|perdon|adios|deseo (?:salir|interrumpir))(?:\b|$)", re.IGNORECASE)
saludo_RE = re.compile(r"\b(hola|buenas|que tal|hey)\b", re.IGNORECASE)

qa = {
    1:"Nu te ofrece tarjeta de crédito Mastercard Gold, y si abres tu Cuenta Nu, te mandamos tu tarjeta de débito para compras físicas.",
    2:"Todo lo podrás hacer de manera digital, sin filas ni papeleo.",
    3:"En nuestro sitio web y en menos de 3 minutos.",
    4:"En tu historial crediticio y otros factores.",
    5:"Claro, conoce todos nuestros aliados de MSI en www.nu.com.mx/meses-sin-intereses-con-nu/",
    6:"Para realizar una reclamación en Nu como persona perteneciente a grupos en situación de vulnerabilidad, puedes comunicarte al teléfono o a través del chat dentro de la app.",
    7:"Puedes registrar la que tú prefieras: tarjeta Nu virtual o física. Si luego eliminas la virtual, tendrás que volver a agregarla.",
    8:"Apple Pay no cobra comisiones; pagar es sin cargo adicional más allá del monto de tu compra.",
    9:"Con Nu y Apple Pay puedes hacer compras internacionales en terminales que acepten Mastercard y pagos contactless.",
    10:"La primera tarjeta agregada a Wallet queda como predeterminada. Para cambiarla, muévela al frente antes de pagar.",
    11:"En Nu buscamos dar aumentos constantes y paulatinos; por ahora puede parecer pequeño.",
    12:"Usa tu tarjeta y paga por lo menos el pago mínimo a tiempo.",
    13:"Buscamos que tengas buen control de tus finanzas. Evaluamos varios aspectos para definir tu línea de crédito.",
    14:"Hasta 7 días hábiles desde que creas tu perfil o pides reposición.",
    15:"Desde la app, toca el botón “invitar amigos”.",
    16:"No te preocupes, si invitas a alguien y no paga, esto no te afecta.",
    17:"Pídele una invitación a alguien que ya tenga su tarjeta Nu.",
    18:"Por el momento no tenemos una recompensa específica.",
    19:"Compártela por el canal que prefieras.",
    20:"Tienes más posibilidades de obtener la tarjeta Nu.",
    21:"Para darte más seguridad al hacer compras o pagos en línea te damos una tarjeta virtual además de la física.",
    22:"No hay cobros ocultos. Solo existe una comisión por pago tardío ($116 o $348 IVA incl., según tu límite). Si pagas a tiempo, no la pagas.",
    23:"Consulta en la app, en el botón “pagar”, para ver todas las opciones.",
    24:"Depende de tu perfil y puede ir aumentando.",
    25:"Significa que el análisis puede tardar hasta 3 meses."
}

patrones_ordenados = [
    (3,  r"\b(como|cómo)\b.*\b(solicitar|aplicar|pedir)\b.*\b(tarjeta|credito)\b|"
         r"\b(solicitar|aplicar|pedir)\b.*\b(tarjeta|credito)\b"),
    (5,  r"\b(msi|meses sin intereses)\b"),
    (6,  r"\b(reclamacion|reclamación)\b.*\b(vulnerab|situacion de vulnerabilidad|grupo vulnerable)\b"),
    (7,  r"\bregistrar\b.*\b(tarjeta)\b.*\b(fisica|virtual)\b|\bregistrar\b.*\b(virtual|fisica)\b"),
    (8,  r"\b(apple ?pay)\b.*\b(gratis|comision|comisión|costo|cargo)\b"),
    (9,  r"\b(comprar|usar|pagar)\b.*\b(fuera de mexico|extranjero|internacional)\b"),
    (10, r"\b(predeterminada|default)\b|\bmover\b.*\bfrente\b.*\b(pagar|transaccion|transacción)\b"),
    (11, r"\b(aumento)\b.*\b(pequeno|pequeño|bajo)\b"),
    (12, r"\b(como|cómo)\b.*\b(aumentar|incrementar)\b.*\b(linea|credito)\b|\bincrementar\b.*\blinea\b"),
    (13, r"\b(linea|l[íi]nea)\b.*\b(baja|muy baja)\b|\bpor que\b.*\b(linea|credito)\b.*\b(baja)\b"),
    (14, r"\b(en cuanto|cuanto|en cuánto|cuánto)\b.*\b(tiempo)\b.*\b(recibir|llega)\b|\bentrega\b.*\btarjeta\b"),
    (15, r"\b(como|cómo)\b.*\binvitar\b|\binvitar\b.*\b(alguien|amigos?)\b"),
    (16, r"\binvito\b.*\bno paga\b|\bsi invito\b.*\bno paga\b|\bno pago\b"),
    (17, r"\b(donde|dónde)\b.*\b(invita|invitacion|invitación)\b|\bconseguir\b.*\binvitacion\b"),
    (18, r"\b(que|qué)\b.*\b(da|ofrece)\b.*\bsi invito\b|\brecompensa\b.*\binvitar\b"),
    (19, r"\b(donde|dónde)\b.*\bcompartir\b.*\binvitacion\b|\bcompartir\b.*\binvitacion\b"),
    (20, r"\bbeneficios?\b.*\binvitacion\b|\bventajas?\b.*\bcon invitacion\b"),
    (21, r"\btarjeta\b.*\bvirtual\b.*\bademas\b.*\bfisica\b|\bpor que\b.*\btarjeta\b.*\bvirtual\b"),
    (22, r"\b(comisiones|cobros ocultos|anualidad|comision.*tardio|comisión.*tardío)\b"),
    (23, r"\b(como|cómo)\b.*\bpagar\b.*\btarjeta\b|\bopciones\b.*\bpago\b|\bboton\b.*\bpagar\b"),
    (24, r"\b(que|qué)\b.*\b(linea)\b.*\bobtener\b|\bcual\b.*\blinea\b.*\bcredito\b"),
    (25, r"\b(lista de espera|estoy en espera|cuanto tarda el analisis|cuánto tarda el análisis)\b"),
    (2,  r"\b(requisitos?|requerimientos?)\b|\bque necesito\b|\bdocumentos?\b|\bpasos\b.*\baplicar\b"),
    (4,  r"\b(aprobar|aprobacion|aprobación)\b|\ben que se basan\b|\bcriterios?\b.*\bsolicitud\b"),
    (1,  r"\btipo de tarjeta\b|"
         r"\bla tarjeta\b.*\b(debito|credito)\b|"
         r"\b(debito|credito)\b.*\b(tarjeta|nu)\b")
]
patrones_compilados = [(pid, re.compile(pat)) for pid, pat in patrones_ordenados]

def run_chatbot_nu():
    print("¡Hola! Soy el Chatbot de NU México. ¿En qué puedo ayudarte hoy?")
    print("Escribe tu duda en lenguaje natural (o escribe 'salir' para terminar).")
    while True:
        user_raw = pedir_no_vacio("> ")
        user = normaliza(user_raw)

        if salir_RE.search(user):
            print("¡Gracias por contactarnos! Fue un placer ayudarte.")
            break

        if saludo_RE.search(user):
            print("¡Hola! Cuéntame, ¿sobre qué te gustaría saber? (por ejemplo: solicitar tarjeta, MSI, Apple Pay, línea de crédito, etc.)")
        else:
            encontrado = False
            for pid, patron in patrones_compilados:
                if patron.search(user):
                    print(qa[pid]); encontrado = True; break
            if not encontrado:
                print("No logré entender tu consulta. ¿Podrías intentarlo de nuevo o formularla de otra manera?")

        seguir_raw = pedir_no_vacio("¿Necesitas ayuda con algo más? (Escribe 'salir' para terminar) \n> ")
        seguir = normaliza(seguir_raw)
        if salir_RE.search(seguir):
            print("¡Gracias por contactarnos! Fue un placer ayudarte.")
            break
        # Procesa inmediatamente la nueva consulta:
        user = seguir
        encontrado = False
        for pid, patron in patrones_compilados:
            if patron.search(user):
                print(qa[pid]); encontrado = True; break
        if not encontrado:
            print("No logré entender tu consulta. Te redirijo al inicio.")

# Para uso independiente:  python bot_nu.py
if __name__ == "__main__":
    run_chatbot_nu()
