#inicialización de estados
import re

salir_RE = r"[nN]o|[sS]alir|[mM]e equivoque|[pP]erd[oó]n|[aA]di[óo]s|[dD]eseo (salir|interrumpir)"

tipoTarjeta_RE = r"[dD][ée]bito|[dD]ebito|[cC][ée]dito|[cC]redito|[tT]ipo de tarjeta"
requisitos_RE = r"[rR]equisito(s|)|[nN]ecesito|[aA]brir|[cC]rear|[pP]asos|[dD]ocumentos"
solicitar_RE = r"[sS]olicitar|[pP]edir|[aA]plicar|[qQ]uiero"
pagar_RE = r"[tT]arifa|[cC]omisi[óo]n|[cC]osto|[aA]nualidad|[mM]eses|[mM]eses sin interes[eé]s|[mM]anejo de cuenta|[iI]nter[eé]s"
problemas_RE = r"[rR]eclamaci[óo]n|[pP]erd[íi]|[pP]erdida|[rR]obo|[bB]loquear|[cC]ancelar|[dD]eshabilitar"
aprobacion_RE = r"[aA]probar|[aA]probaci[óo]n|[sS]olicitud|[bB]asan|[bB]asan|[hH]istorial crediticio"
lineaCredito_RE = r"[lL][íi]nea|[aA]umento|[cC]r[ée]dito (bajo|pequeño)|[pP]or qu[ée] (bajo|pequeño)|[mM]uy poco|[iI]ncrementar"
entrega_RE = r"[eE]ntrega|[tT]iempo de entrega|[cC]u[áa]ndo llega|[dD]omicilio|[rR]ecibir"
invitar_RE = r"[iI]nvitaci[óo]n|[iI]nvitado|[iI]nvitando|[iI]nvito|[cC]ódigo|[cC]ompartir"
beneficios_RE = r"[bB]eneficio(s|)|[vV]entaja(s|)|[qQ]u[ée] ofrece|[qQ]u[ée] tiene|[vV]irtual|[fF][íi]sica"
seguridad_RE = r"[sS]eguro|[sS]eguridad|[pP]rotegen|[dD]atos|[pP]rivacidad|[cC]lave"
banco_RE = r"[bB]anco|[eE]mpresa|[fF]inanciera|[sS]ociedad"
ApplePay_RE = r"[aA]pple [pP]ay|[aA]pple[pP]ay|[aA]pple|[cC]omision(es|)|[gG]ratis|[gG]ratuito|[cC]osto|[cC]obra|[cC]argo"
Internacional_RE = r"[iI]nternacional|[fF]uera [dD]e [mM][ée]xico|[eE]xtranjero|[vV]iaje"


state = 0
Salida = 1

print("¡Hola! Soy el Chatbot de NU México ¿En qué puedo ayudarte hoy?")

while Salida:
    if state == 0:
        opcion = input("Puedo ayudarte con: apertura de cuenta, transferencias, tarjetas, límites o problemas con la app. \n\t\t\t")
        if re.findall(tipoTarjeta_RE, opcion, flags=0) != []:
            state = 1
        elif re.findall(requisitos_RE, opcion, flags=0) != []:
            state = 2
        elif re.findall(solicitar_RE, opcion, flags=0) != []:
            state = 3
        elif re.findall(pagar_RE, opcion, flags=0) != []:
            state = 4
        elif re.findall(problemas_RE, opcion, flags=0) != []:
            state = 5
        elif re.findall(aprobacion_RE, opcion, flags=0) != []:
            state = 6
        elif re.findall(lineaCredito_RE, opcion, flags=0) != []:
            state = 7
        elif re.findall(entrega_RE, opcion, flags=0) != []:
            state = 8
        elif re.findall(invitar_RE, opcion, flags=0) != []:
            state = 9
        elif re.findall(beneficios_RE, opcion, flags=0) != []:
            state = 10
        elif re.findall(seguridad_RE, opcion, flags=0) != []:
            state = 11 
        elif re.findall(banco_RE, opcion, flags=0) != []:
            state = 12        
        elif re.findall(ApplePay_RE, opcion, flags=0) != []:
            state = 13
        elif re.findall(Internacional_RE, opcion, flags=0) != []:
            state = 14 
        
        elif re.findall(salir_RE, opcion, flags=0) != []:
            state = 16
        else:
            state = 17
        continue

    if state == 1:
        print("""Nu te ofrece tarjeta de crédito Mastecard Gold, y si abres tu Cuenta Nu, 
              te mandamos tu tarjeta de débito para compras físicas.""")
        state = 15
        continue

    if state == 2:
        print("""Todo lo podrás hacer de manera digital, sin filas ni papeleo.""")
        state = 15
        continue

    if state == 3:
        print("""En nuestro sitio web y en menos de 3 minutos.""")
        state = 15
        continue

    if state == 4:
        print("""conoce todos nuestros aliados de MSI en www.nu.com.mx/meses-sin-intereses-con-nu/""")
        state = 15
        continue

    if state == 5:
        print("""Para realizar una reclamación en Nu como persona perteneciente a grupos en situación de vulnerabilidad, 
              puedes comunicarte al teléfono o a través del chat dentro de la app.""")
        state = 15
        continue

    if state == 6:
        print("""En tu historial crediticio y otros factores.""")
        state = 15
        continue
    
    if state == 7:
        print("""La clave es: usa tu tarjeta de crédito y paga por lo menos el pago mínimo a tiempo.
              Nosotros buscamos que tengas buen control sobre tus finanzas y deseamos que tu capacidad de pago no sobrepase tu crédito. 
              Por eso, para definir tu línea de crédito, evaluamos vários aspectos.""")
        state = 15
        continue
    
    if state == 8:
        print("""Hasta 7 días hábiles a partir de la creación de tu perfil o solicitud de reposición de tu tarjeta.""")
        state = 15
        continue   

    if state == 9:
        print("""Desde la app, selecciona el botón de "invitar amigos".
              Puedes pedirle una invitación a alguien que ya tenga su tarjeta Nu.
              Puedes compartirlo por el canal que prefieras.
              Tienes más posibildades de obtener la tarjeta Nu.
              """)
        state = 15
        continue  

    if state == 10:
        print("""Te damos una Tarjeta Virtual y Fisica para darte más seguridad al hacer 
              compras o pagos en línea. Ademas te ofrecemos $0 anualidad, sin comisiones sorpresa y muchos más.
              """)
        state = 15
        continue  

    if state == 11:
        print("""Nu es completamente segura, desarrollamos tecnología solo para esto.
              """)
        state = 15
        continue 
    
    if state == 12:
        print("""Somos una Sociedad Financiera Popular que opera como empresa de tecnología que ofrece servicios financieros..
              """)
        state = 15
        continue  

    if state == 13:
        print("""Apple Pay no cobra comisiones, así que podrás hacer las compras que quieras sin ningún cargo adicional o 
                 comisión al pagar, más allá del monto de tu compra.
              """)
        state = 15
        continue 
    
    if state == 14:
        print("""Nu y Apple Pay puedes hacer compras internacionales en las terminales que acepten Mastercard y pagos contactless.
              """)
        state = 15
        continue 

    if state == 15:
        opcion = input("¿Necesitas ayuda con algo más?  \n\t\t\t")
    
        if re.findall(salir_RE, opcion, flags=0) != []:
            state = 16
        else:
            if re.findall(tipoTarjeta_RE, opcion, flags=0) != []:
                state = 1
            elif re.findall(requisitos_RE, opcion, flags=0) != []:
                state = 2
            elif re.findall(solicitar_RE, opcion, flags=0) != []:
                state = 3
            elif re.findall(pagar_RE, opcion, flags=0) != []:
                state = 4
            elif re.findall(problemas_RE, opcion, flags=0) != []:
                state = 5
            elif re.findall(aprobacion_RE, opcion, flags=0) != []:
                state = 6
            elif re.findall(lineaCredito_RE, opcion, flags=0) != []:
                state = 7
            elif re.findall(entrega_RE, opcion, flags=0) != []:
                state = 8
            elif re.findall(invitar_RE, opcion, flags=0) != []:
                state = 9
            elif re.findall(beneficios_RE, opcion, flags=0) != []:
                state = 10
            elif re.findall(seguridad_RE, opcion, flags=0) != []:
                state = 11 
            elif re.findall(banco_RE, opcion, flags=0) != []:
                state = 12
            elif re.findall(ApplePay_RE, opcion, flags=0) != []:
                state = 13
            elif re.findall(Internacional_RE, opcion, flags=0) != []:
                state = 14 
            
            elif re.findall(salir_RE, opcion, flags=0) != []:
                state = 16
            else:
                print("No logré entender tu consulta. Te redirijo al menú principal.")
                state = 0
        continue

    if state == 16:
        print("¡Gracias por contactarnos! Fue un placer ayudarte.")
        Salida = 0
        continue

    if state == 17:
        print("No logré entender tu consulta. ¿Podrías intentarlo de nuevo?")
        state = 0
        continue