# -*- coding: utf-8 -*-
# Cada slide: (label, clases_section, steps, cuerpo_html, notas)
S = []
def add(label, body, notes, steps=1, cls=""):
    S.append((label, cls, steps, body, notes))

K = lambda pose, style: f'<img class="kori" src="assets/kori/{pose}.png" alt="Kori, mascota del Student Community Day" style="{style}">'

# 01 COVER -------------------------------------------------------------
add("Portada", f'''
    <img src="assets/img/cristo.png" alt="" style="position:absolute;left:0;top:0;height:1080px;z-index:0">
    {K("alegre","right:140px;bottom:130px;width:230px")}
    <div class="pad" style="justify-content:center;padding-left:640px">
      <div class="eyebrow">Student Community Day · Cochabamba</div>
      <h1 class="cover" style="font-size:108px;line-height:1.02">De programar con IA<br>a construir con <span class="grad-word">agentes</span></h1>
      <div class="subtitle" style="font-family:var(--cs-font-mono);font-size:32px;letter-spacing:.06em;margin-top:34px">Harness · Skills · Loops · Orquestación con Orca</div>
      <div class="payoff" style="margin-top:44px;color:var(--scd-cyan)">10 OCTUBRE 2026</div>
    </div>''',
    "Antes de presentarme, lanzo una tarea real a tres agentes en Orca y los dejo corriendo en la pantalla de al lado. Vamos a volver a ellos más tarde. Hoy no vengo a contarles cómo usar agentes, sino cómo se construye el sistema donde trabajan.",
    cls="grad")

# 02 SPEAKER ------------------------------------------------------------
add("Speaker", f'''
    <div style="position:absolute;left:230px;top:200px;width:620px;height:620px;border-radius:50%;padding:12px;background:conic-gradient(from 200deg, var(--scd-cyan) 0 55%, var(--scd-lime) 55% 72%, rgba(31,211,245,.18) 72% 100%)">
      <img src="assets/img/speaker.jpg" alt="Foto de Rodrigo Torrico" style="width:100%;height:100%;border-radius:50%;object-fit:cover;display:block;border:8px solid var(--scd-navy)">
    </div>
    {K("asomado","left:430px;top:105px;width:230px")}
    <div class="pad" style="justify-content:center;padding-left:960px">
      <div class="eyebrow">Quién te habla</div>
      <h2 class="title" style="font-size:120px;margin-bottom:30px">Rodrigo<br>Torrico</h2>
      <div style="font-size:32px;line-height:1.5;color:#fff">Senior Software Engineer · Unosquare<br><span style="color:var(--cs-body)">7 años full-stack · Founder SaaS<br>Mentor de otros devs</span></div>
      <div style="display:flex;flex-direction:column;gap:18px;margin-top:46px">
        <div style="display:flex;gap:22px;align-items:center"><span class="chip lime" style="min-width:150px;text-align:center">Instagram</span><span class="mono" style="font-size:40px;color:var(--scd-cyan)">@tokidev.ai</span></div>
        <div style="display:flex;gap:22px;align-items:center"><span class="chip" style="min-width:150px;text-align:center">GitHub</span><span class="mono" style="font-size:40px;color:var(--scd-cyan)">@tokidev-ai</span></div>
      </div>
    </div>''',
    "Me presento en 30 segundos: soy Rodrigo Torrico, Senior Software Engineer en Unosquare, siete años haciendo full-stack, construyo productos SaaS y mentoreo a otros devs. Todo lo que van a ver hoy lo uso en mi trabajo diario. Si quieren el material y más contenido sobre agentes: Instagram @tokidev.ai y GitHub @tokidev-ai.",
    steps=1)

# 02 GANCHO 0 LINEAS --------------------------------------------------
add("Gancho cero lineas", f'''
    {K("sorprendido","right:150px;bottom:160px;width:380px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">Antes de empezar</div>
      <h2 class="title reveal r-rise" data-step="1" style="max-width:1300px">Un millón de líneas. ¿Cuántas a mano?</h2>
      <div style="display:flex;align-items:flex-end;gap:80px">
        <div class="reveal r-scale" data-step="2">
          <div class="big" style="font-size:300px;color:var(--scd-lime)">0</div>
        </div>
        <div class="reveal r-left" data-step="3" style="display:flex;flex-direction:column;gap:22px;padding-bottom:30px">
          <div style="font-size:34px;color:#fff"><span class="cyan mono">3</span> personas · <span class="cyan mono">5</span> meses · <span class="cyan mono">+1.500</span> PRs</div>
          <div class="stat-source">Fuente: OpenAI, Harness engineering, febrero 2026</div>
        </div>
      </div>
    </div>''',
    "Pregunta a la sala: un equipo de OpenAI construyó un producto de casi un millón de líneas en cinco meses. ¿Cuántas escribieron a mano? Dejo que respondan. Cero. Eran tres personas y más de mil quinientos PRs. El trabajo humano no desapareció: se movió al entorno. Y la promesa: al final de la charla vas a saber exactamente qué hacer el lunes, y volvemos a esos tres agentes.",
    steps=3)

# 03 AGENDA ------------------------------------------------------------
agenda = [("01","Dónde estamos"),("02","Harness"),("03","Skills"),("04","Loops"),("05","Orca"),("06","Tu ruta")]
items = "".join(f'''<div class="reveal r-rise" data-step="2" style="display:flex;flex-direction:column;align-items:center;gap:20px;width:200px"><div class="ring{' lime' if n=='06' else ''}">{n}</div><div style="font-size:28px;color:#fff;text-align:center">{t}</div></div>''' for n,t in agenda)
add("Agenda", f'''
    {K("guinando","right:150px;top:110px;width:300px")}
    <div class="pad mid">
      <div class="eyebrow reveal" data-step="1">El viaje de hoy</div>
      <h2 class="title reveal r-rise" data-step="1">Seis paradas, un proyecto</h2>
      <div class="stagger" style="display:flex;justify-content:space-between;margin-top:40px;position:relative">
        <div class="slant reveal r-wipe" data-step="2" style="position:absolute;left:100px;right:100px;top:40px;height:8px;clip-path:none;opacity:.5"></div>
        {items}
      </div>
      <div class="payoff reveal r-mask" data-step="3" style="margin-top:70px">Al final: tu plan para el lunes</div>
    </div>''',
    "Este es el recorrido. Todo lo vamos a aplicar a un solo proyecto real (aquí cuento cuál es el mío). En cada parada el proyecto mejora algo visible. Y la última parada es la que más les importa: qué hacer el lunes.",
    steps=3)

# 04 DONDE ESTAMOS -----------------------------------------------------
add("Donde estamos", f'''
    <div class="skew reveal r-blur" data-step="1" style="right:150px;top:250px;width:880px;height:560px"><img src="assets/img/laptop.jpg" alt="Desarrollador trabajando en una laptop con código"></div>
    {K("asomado","right:560px;top:150px;width:260px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">01 · Dónde estamos</div>
      <h2 class="title reveal r-rise" data-step="1" style="max-width:800px">Usar agentes<br>ya es el piso</h2>
      <div class="stagger" style="display:flex;flex-direction:column;gap:26px;max-width:760px">
        <div class="reveal r-left" data-step="2" style="display:flex;align-items:baseline;gap:28px"><div class="big" style="font-size:110px" data-counter="90" data-target-step="2">0<span class="unit">%</span></div><div style="font-size:28px">usa agentes de código cada semana</div></div>
        <div class="reveal r-left" data-step="2" style="display:flex;align-items:baseline;gap:28px"><div class="big" style="font-size:110px" data-counter="68" data-target-step="2">0<span class="unit">%</span></div><div style="font-size:28px">los usa todos los días</div></div>
        <div class="reveal r-left" data-step="2" style="display:flex;align-items:baseline;gap:28px"><div class="big lime" style="font-size:110px;color:var(--scd-lime)" data-counter="47" data-target-step="2">0<span class="unit">%</span></div><div style="font-size:28px">de su código lo escribe un agente</div></div>
      </div>
      <div class="stat-source reveal" data-step="2" style="margin-top:22px">JetBrains, 2026, +15.000 devs (vía charla Agent First)</div>
    </div>''',
    "En 2026 usar agentes dejó de ser ventaja: es el piso. Nueve de cada diez devs los usan cada semana y casi la mitad del código ya lo escribe un agente. Lo que diferencia ahora es qué tan bien está armado el sistema alrededor del agente. Verificar la cifra en la fuente original de JetBrains antes de presentar.",
    steps=2)

# 05 BRECHA ------------------------------------------------------------
add("Brecha de confianza", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">01 · Dónde estamos</div>
      <h2 class="title reveal r-rise" data-step="1">Confiamos poco y revisamos menos</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:70px;margin-top:20px">
        <div class="reveal r-scale" data-step="2">
          <div class="big" style="font-size:200px;color:var(--scd-cyan)" data-counter="96" data-target-step="2">0<span class="unit">%</span></div>
          <div class="slant reveal r-wipe" data-step="2" style="width:96%;margin:20px 0 22px"></div>
          <div style="font-size:32px;color:#fff">no confía del todo en el código de la IA</div>
        </div>
        <div class="reveal r-scale" data-step="3">
          <div class="big" style="font-size:200px;color:var(--scd-red)" data-counter="48" data-target-step="3">0<span class="unit">%</span></div>
          <div class="slant reveal r-wipe" data-step="3" style="--c:var(--scd-red);width:48%;margin:20px 0 22px"></div>
          <div style="font-size:32px;color:#fff">lo revisa siempre antes del commit</div>
        </div>
      </div>
      <div class="stat-source reveal" data-step="3" style="margin-top:40px">Sonar, enero 2026</div>
    </div>''',
    "Casi nadie confía del todo en el código que genera la IA, pero solo la mitad lo revisa siempre antes de hacer commit. Esa brecha es el problema que vamos a resolver hoy: no con más desconfianza, sino con un sistema que verifique por nosotros. Broma posible: revisión del PR de mil líneas, LGTM.",
    steps=3)

# 06 ESCALERA SHAPIRO --------------------------------------------------
levels = [("L0","Autocompletado"),("L1","Pasante"),("L2","Junior que revisas línea a línea"),("L3","Dev que revisas sin escribir"),("L4","Equipo: tú escribes specs"),("L5","Fábrica oscura")]
lv = ""
for i,(l,t) in enumerate(levels):
    hl = (l=="L2")
    col = "var(--scd-lime)" if hl else "var(--scd-cyan)"
    lv += f'''<div class="reveal r-rise" data-step="2" style="position:absolute;left:{i*205}px;bottom:{i*62}px;width:195px">
      <div style="font-family:var(--cs-font-heading);font-size:58px;color:{col}">{l}</div>
      <div style="font-size:23px;line-height:1.25;color:{'#fff' if hl else 'var(--cs-body)'};min-height:60px">{t}</div>
      <div class="slant" style="--c:{col};height:{'18' if hl else '10'}px;margin-top:10px;clip-path:none"></div></div>'''
add("Escalera de niveles", f'''
    {K("curioso","right:150px;bottom:160px;width:300px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">01 · Dónde estamos</div>
      <h2 class="title reveal r-rise" data-step="1">¿En qué nivel estás?</h2>
      <div class="stagger" style="position:relative;height:500px;width:1240px">{lv}
        <div class="chip lime reveal r-scale" data-step="3" style="position:absolute;left:410px;bottom:20px;background:rgba(2,13,34,.9)">~90% está aquí</div>
      </div>
      <div class="stat-source reveal" data-step="2">Niveles de Dan Shapiro, enero 2026</div>
    </div>''',
    "Momento interactivo: mano alzada. ¿Quién está en L0, autocompletado? ¿L1? ¿L2, un junior al que revisas línea por línea? ¿L3? Según Shapiro, cerca del 90% de quienes se dicen AI native está en L2 sin saberlo. Pregunta: ¿qué te impide subir uno? Casi siempre es contexto, verificación o confianza. Eso es lo que cubre el resto de la charla. En mi proyecto: le pedí una función, la hizo, pero a su manera. Funcionó, pero no era lo que quería.",
    steps=3)

# 07 METR ----------------------------------------------------------------
add("Adivina el resultado", f'''
    {K("pensando","right:150px;top:110px;width:270px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">01 · Impacto real</div>
      <h2 class="title reveal r-rise" data-step="1" style="max-width:1300px">Devs expertos con IA: ¿más rápidos o más lentos?</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:56px;max-width:1450px">
        <div class="hud reveal r-scale" data-step="2" data-overlap-ok>
          <div class="tag">Lo que creían</div>
          <div class="big" style="font-size:150px;margin-top:14px;color:var(--scd-cyan)">+20<span class="unit">%</span></div>
          <p>más rápidos</p>
        </div>
        <div class="hud red reveal r-scale" data-step="3" data-overlap-ok>
          <div class="tag">Lo que se midió</div>
          <div class="big" style="font-size:150px;margin-top:14px;color:var(--scd-red)">−19<span class="unit">%</span></div>
          <p>más lentos</p>
        </div>
      </div>
      <div class="stat-source reveal" data-step="3" style="margin-top:30px">METR, 2025. Su seguimiento de feb. 2026 sugiere más aceleración hoy</div>
    </div>''',
    "Antes de mostrar el dato, la sala adivina: devs experimentados, en repos que conocen, con IA, ¿más rápidos o más lentos? Voto a mano alzada. Revelo: creían ser 20% más rápidos y fueron 19% más lentos. La lección no es que la IA frene: es que la percepción no es medición. Matiz honesto: el propio METR, en su seguimiento de febrero de 2026 con 57 devs y más de 800 tareas, dice que probablemente hoy hay más aceleración. No citar el 19% como hecho actual.",
    steps=3)

# 08 AMPLIFICA -----------------------------------------------------------
add("La IA amplifica", f'''
    {K("confiado","right:150px;bottom:160px;width:300px")}
    <div class="pad" style="justify-content:center">
      <div class="quote reveal r-blur" data-step="1" style="max-width:1230px">
        <blockquote>La IA amplifica: si tu base es buena, mejor. Si es caos, más caos</blockquote>
        <cite>DORA 2025 · Faros · Stanford</cite>
      </div>
      <div class="payoff reveal r-mask" data-step="2" style="margin-top:50px;color:var(--scd-cyan)">Mide entrega con DORA o DX Core 4, no con sensaciones</div>
    </div>''',
    "DORA 2025: más del 80% reporta mejor productividad, pero varios análisis ven que la ganancia individual se diluye a nivel de equipo y la estabilidad puede empeorar. La IA es un amplificador. El cuello de botella se movió de escribir código a revisar y dar contexto. Para los estudiantes: ganan más velocidad bruta pero arriesgan su aprendizaje. Usen los agentes para entender, no solo para producir.",
    steps=2)

# 09 TRANSICION HARNESS ------------------------------------------------
add("Transicion harness", f'''
    {K("emocionado","right:160px;bottom:150px;width:250px")}
    <div class="pad center">
      <div class="eyebrow">02 · Harness</div>
      <h1 class="ts-title" style="font-size:150px">Agent = Model + <span class="grad-word">Harness</span></h1>
      <div class="ts-tagline" style="max-width:1050px">El caballo es fuerte. Sin arnés, no tira del carro hacia donde quieres</div>
    </div>''',
    "Un agente es un modelo dentro de un harness: todo lo que decide qué ve el modelo, qué herramientas usa, cómo recuerda, cómo se verifica su trabajo y qué tiene permitido hacer. Analogía: el arnés de un caballo, o el tablero de un auto. El término lo popularizó Mitchell Hashimoto y lo desarrolló OpenAI con el experimento de cero líneas.")

# 10 EVOLUCION ---------------------------------------------------------
evo = [("Prompt engineering","Lenguaje","Cómo pides",""),("Context engineering","Información","Qué ve el modelo",""),("Harness engineering","Entorno","Cómo actúa y se corrige"," lime")]
ev = ""
for i,(a,b,c,cl) in enumerate(evo):
    ev += f'''<div class="hud{cl} reveal r-rise" data-step="{i+2}" style="flex:1;min-height:330px"><div class="tag">{b}</div><h3>{a}</h3><p>{c}</p></div>'''
    if i<2: ev += f'<div class="reveal r-fade" data-step="{i+3}" style="font-size:60px;color:var(--scd-cyan);align-self:center">›</div>'
add("Del prompt al entorno", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">02 · Harness</div>
      <h2 class="title reveal r-rise" data-step="1">Del prompt al entorno</h2>
      <div style="display:flex;gap:28px;align-items:stretch">{ev}</div>
      <div class="payoff reveal r-mask" data-step="4" style="margin-top:50px">No mejores el prompt, mejora el entorno</div>
    </div>''',
    "Tres capas que son la línea de tiempo de estos años. Prompt engineering: cómo redactas la petición. Context engineering: qué información ve el modelo. Harness engineering: cómo actúa y se corrige el agente. La lección central de OpenAI: cuando un agente falla, no es un problema de prompt; es una capacidad, un contexto o una estructura que falta en el entorno.",
    steps=4)

# 11 REGLA PREGUNTA REPETIDA -------------------------------------------
add("La pregunta repetida", f'''
    {K("saludando","right:150px;bottom:160px;width:340px")}
    <div class="pad" style="justify-content:center">
      <div class="eyebrow reveal" data-step="1">Levanta la mano si…</div>
      <div class="reveal r-rise" data-step="1" style="font-size:44px;color:#fff;max-width:1150px;line-height:1.3;margin-bottom:60px">le explicaste lo mismo dos veces a un agente</div>
      <div class="quote reveal r-blur" data-step="2" style="max-width:1250px">
        <blockquote style="font-size:72px">Cada pregunta que un agente te hace dos veces es una decisión que no documentaste</blockquote>
        <cite>Pedro Anze · Agent First</cite>
      </div>
    </div>''',
    "Momento interactivo: que levante la mano quien le haya explicado lo mismo dos veces a un agente. Casi todos. Esta regla es harness engineering en una frase. En mi proyecto: el agente me preguntó por tercera vez cómo correr los tests. Lo escribí en AGENTS.md y dejó de preguntar.",
    steps=2)

# 12 GUIAS Y SENSORES --------------------------------------------------
add("Guias y sensores", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">02 · Harness</div>
      <h2 class="title reveal r-rise" data-step="1">Guías antes, sensores después</h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:56px">
        <div class="hud reveal r-left" data-step="2" style="min-height:430px">
          <div class="tag">Feedforward · antes de actuar</div>
          <h3 style="font-size:76px">Guías</h3>
          <div class="chips" style="margin-top:24px"><span class="chip">AGENTS.md</span><span class="chip">skills</span><span class="chip">convenciones</span><span class="chip">docs de diseño</span><span class="chip">scripts de arranque</span></div>
        </div>
        <div class="hud lime reveal r-left" data-step="3" style="min-height:430px">
          <div class="tag">Feedback · durante y después</div>
          <h3 style="font-size:76px">Sensores</h3>
          <div class="chips" style="margin-top:24px"><span class="chip lime">linters</span><span class="chip lime">tipos</span><span class="chip lime">tests</span><span class="chip lime">agente revisor</span><span class="chip lime">observabilidad</span></div>
        </div>
      </div>
    </div>''',
    "Un modelo mental útil. Las guías actúan antes de que el agente actúe: AGENTS.md, skills, convenciones, documentos de diseño. Los sensores actúan durante o después: lint, tipos, tests, revisión por otro agente. Un buen harness tiene las dos cosas. Aquí va el fallo en vivo: muestro un caso preparado donde el agente cambia algo fuera de alcance y un test o una regla lo detecta.",
    steps=3)

# 13 AGENTS.MD -----------------------------------------------------------
add("AGENTS.md", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">02 · Harness</div>
      <h2 class="title reveal r-rise" data-step="1">Empieza por un archivo</h2>
      <div style="display:grid;grid-template-columns:1.15fr .85fr;gap:70px;align-items:center">
        <div class="term reveal r-blur" data-step="2">
          <div class="bar"><i></i><i></i><i></i><span>AGENTS.md</span></div>
<pre><span class="p"># Proyecto</span>
API de reservas del centro de estudiantes
<span class="p">## Cómo correrlo</span>
<span class="ok">pnpm dev</span>  ·  <span class="ok">pnpm test</span>
<span class="p">## Convenciones</span>
Código en inglés
<span class="p">## Decisiones tomadas</span>
<span class="dim">No tocar /payments sin aprobación</span></pre>
        </div>
        <div class="reveal r-left" data-step="3">
          <div class="big" style="font-size:66px;line-height:1.05;text-transform:uppercase">Actualízalo cada vez que el agente <span class="lime">falle</span></div>
          <div class="stat-source" style="margin-top:24px">Regla de Greg Brockman</div>
        </div>
      </div>
    </div>''',
    "AGENTS.md en la raíz del repo: qué es el proyecto, cómo correrlo, convenciones y decisiones ya tomadas. Funciona en Claude Code, Codex y la mayoría de agentes. La regla de Brockman: actualízalo cada vez que el agente falle. Cambiar el ejemplo por el AGENTS.md real de mi proyecto.",
    steps=3)

# 14 SEIS PASOS ------------------------------------------------------------
steps6 = [("AGENTS.md","En la raíz del repo"),("Repo legible","Planes dentro del repo"),("Sensores","Lint, tipos y tests"),("Observable","Logs y trazas"),("Revisor","Decide un humano"),("Itera","Fallo repetido, nueva regla")]
g = ""
for i,(t,d) in enumerate(steps6):
    g += f'''<div class="reveal r-rise" data-step="2" style="display:flex;gap:26px;align-items:center"><div class="ring{' lime' if i==5 else ''}">0{i+1}</div><div><div style="font-family:var(--cs-font-heading);font-size:40px;text-transform:uppercase;color:#fff">{t}</div><div style="font-size:24px;color:var(--cs-body)">{d}</div></div></div>'''
add("Harness en seis pasos", f'''
    {K("aplaudiendo","right:160px;bottom:150px;width:240px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">02 · Harness</div>
      <h2 class="title reveal r-rise" data-step="1">Tu harness en seis pasos</h2>
      <div class="stagger" style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:80px 50px;margin-top:50px;max-width:1350px">{g}</div>
    </div>''',
    "Cómo construir un harness, paso a paso. Uno: AGENTS.md. Dos: repo legible para agentes, el conocimiento vive en el repo y no en tu cabeza. Tres: sensores rápidos que el agente corre solo antes de pedir revisión. Cuatro: que pueda ejecutar y observar la app. Cinco: un agente revisor, con la decisión final en un humano. Seis: itera el harness, no el prompt. Cada fallo repetido se convierte en una regla, un test o una skill.",
    steps=2)

# 15 SKILLS ANATOMIA -------------------------------------------------------
add("Que es una skill", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">03 · Skills</div>
      <h2 class="title reveal r-rise" data-step="1" style="max-width:1500px">MCP le da manos, las skills le dan <span class="grad-word">hábitos</span></h2>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center">
        <div class="term reveal r-blur" data-step="2">
          <div class="bar"><i></i><i></i><i></i><span>mi-skill/</span></div>
<pre><span class="p">SKILL.md</span>      <span class="dim">qué hace y cuándo</span>
<span class="ok">scripts/</span>      <span class="dim">lo que ejecuta</span>
<span class="ok">references/</span>   <span class="dim">lo que consulta</span>
<span class="ok">templates/</span>    <span class="dim">lo que reutiliza</span></pre>
        </div>
        <div class="reveal r-left" data-step="3" data-overlap-ok>
          <div class="big" style="font-size:150px;color:var(--scd-lime)">~100</div>
          <div style="font-size:30px;color:#fff;margin-top:10px">tokens por skill hasta que la tarea coincide</div>
          <div class="chips" style="margin-top:30px"><span class="chip">Claude Code</span><span class="chip">Codex</span><span class="chip">Gemini CLI</span><span class="chip">Cursor</span></div>
        </div>
      </div>
    </div>''',
    "Los MD dan contexto, las skills dan habilidades. Una skill es una carpeta con un SKILL.md que dice qué hace y cuándo, más scripts, referencias y plantillas. Es un estándar abierto que funciona en varios agentes. Se cargan por divulgación progresiva: el agente lee solo nombre y descripción, unos 100 tokens, y abre el resto cuando la tarea coincide. Analogía: las recetas de una cocina. El cocinero sabe cocinar; la receta le dice cómo lo hace tu restaurante.",
    steps=3)

# 16 SKILLS RECOMENDADAS ---------------------------------------------------
sk = [("Superpowers","Planear y probar antes de codificar",""),("systematic-debugging","Depurar con método",""),("frontend-design","Diseño deliberado",""),("pdf · docx · xlsx","Documentos",""),("skill-creator","Tu puerta a constructor"," lime"),("Agent-Browser","Verificación visual","")]
c = "".join(f'''<div class="hud{cl} reveal r-rise" data-step="2" style="padding:32px 36px"><h3 style="font-size:40px;text-transform:none;font-family:var(--cs-font-mono);letter-spacing:0">{n}</h3><p>{d}</p></div>''' for n,d,cl in sk)
add("Skills recomendadas", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">03 · Skills</div>
      <h2 class="title reveal r-rise" data-step="1">Las que más se recomiendan en 2026</h2>
      <div class="stagger" style="display:grid;grid-template-columns:repeat(3,1fr);gap:30px">{c}</div>
    </div>''',
    "Las más recomendadas en los rankings de 2026. Superpowers, de obra: brainstorming, planes, TDD, revisión de código. systematic-debugging, que cambia el comportamiento más frustrante de los agentes. frontend-design de Anthropic, para evitar el look genérico. Las skills de documentos. Y la que más importa para esta charla: skill-creator y mcp-builder, la puerta de entrada a pasar de usuario a constructor. No pongo número de estrellas: varían muchísimo entre fuentes. Dato meta: estas diapositivas se hicieron con una skill (slizdeck).",
    steps=2)

# 17 ELEGIR -----------------------------------------------------------------
crit = ["Resuelve un fallo que ya viste repetirse","Dice con precisión cuándo se activa","Tiene criterio de terminado","Léela antes: corre con tus permisos"]
cr = "".join(f'''<div class="reveal r-left" data-step="2" style="display:flex;gap:24px;align-items:center;font-size:32px;color:#fff"><span class="slant" style="width:46px;height:20px;flex:none"></span>{t}</div>''' for t in crit)
add("Como elegir una skill", f'''
    {K("determinado","right:150px;bottom:160px;width:330px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">03 · Skills</div>
      <h2 class="title reveal r-rise" data-step="1">Instala 2 o 3, <span class="lime">no 20</span></h2>
      <div class="stagger" style="display:flex;flex-direction:column;gap:30px;margin-top:10px">{cr}</div>
      <div class="chip lime reveal r-scale" data-step="3" style="margin-top:50px;align-self:flex-start;font-size:26px">Demo · misma tarea, con skill y sin skill</div>
    </div>''',
    "Cómo elegir: que resuelva un fallo que ya viste repetirse, no uno hipotético; que tenga una descripción precisa de cuándo se activa; manejo de errores y criterio de terminado. Instala dos o tres: cada una compite por la atención del agente. Y léela antes de instalarla: es instrucción que tu agente ejecuta con tus permisos. Demo de 2 minutos: misma tarea en dos agentes, con y sin la skill. En mi proyecto: empaqueté mi forma de planear y revisar en una skill. Ahora lo hace como lo haría yo.",
    steps=3)

# 18 LOOP --------------------------------------------------------------------
nodes = [("01","Meta","Qué es terminado",250,0),("02","Acción","Usa herramientas",520,190),("03","Observación","Lee resultados",250,380),("04","Decisión","Seguir o corregir",-20,190)]
nd = ""
for n,t,d,x,y in nodes:
    nd += f'''<div class="reveal r-scale" data-step="2" style="position:absolute;left:{x}px;top:{y}px;width:300px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:8px"><div class="ring">{n}</div><div style="font-family:var(--cs-font-heading);font-size:38px;text-transform:uppercase;color:#fff">{t}</div><div style="font-size:23px;color:var(--cs-body)">{d}</div></div>'''
add("Loop engineering", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">04 · Loop engineering</div>
      <h2 class="title reveal r-rise" data-step="1">Diseña el ciclo, no el prompt</h2>
      <div style="display:grid;grid-template-columns:820px 1fr;gap:60px">
        <div style="position:relative;height:560px;margin-top:-20px">
          <svg class="reveal r-fade" data-step="2" viewBox="0 0 820 560" style="position:absolute;inset:0;width:820px;height:560px" aria-hidden="true"><ellipse cx="400" cy="236" rx="270" ry="190" fill="none" stroke="#1FD3F5" stroke-opacity=".45" stroke-width="3" stroke-dasharray="10 12"/></svg>
          {nd}
        </div>
        <div style="align-self:center">
          <div class="hud red reveal r-left" data-step="3"><div class="tag">05 · Parada</div><h3>Éxito o tope</h3><p>La verifica una máquina, no el modelo</p></div>
          <div class="payoff reveal r-mask" data-step="4" style="margin-top:40px;color:var(--scd-cyan)">Como un termostato: fijas la meta, él mide y corrige</div>
        </div>
      </div>
    </div>''',
    "Loop engineering: diseñar el sistema de retroalimentación que deja al agente planear, actuar, observar y corregirse hasta cumplir una meta, sin que dirijas cada turno. Cinco partes: meta verificable, acción, observación, decisión y parada, que siempre incluye un tope. Analogía del termostato: no le dices la temperatura cada minuto. Advertencia honesta: es una práctica emergente, aún no es un estándar. Un loop con contexto malo solo falla más rápido y más caro.",
    steps=4)

# 19 TIPOS DE LOOP -------------------------------------------------------------
add("Tipos de loop", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">04 · Loop engineering</div>
      <h2 class="title reveal r-rise" data-step="1">Cuatro loops que ya puedes usar</h2>
      <table class="sz-table" style="max-width:1620px">
        <thead><tr><th>Loop</th><th>Idea</th><th>Ejemplo</th></tr></thead>
        <tbody>
          <tr class="hl reveal" data-step="2"><td class="lead"><span class="mono">/goal</span></td><td>Itera hasta cumplir una condición</td><td>Que pase la suite de tests</td></tr>
          <tr class="reveal" data-step="2"><td class="lead"><span class="mono">/loop</span></td><td>Repite cada cierto tiempo</td><td>Vigilar el CI y arreglar lo trivial</td></tr>
          <tr class="reveal" data-step="2"><td class="lead">Evaluador y optimizador</td><td>Uno genera, otro critica</td><td>Código y revisión en ciclo</td></tr>
          <tr class="reveal" data-step="2"><td class="lead">Monitoreo</td><td>Corre a lo largo del tiempo</td><td>Revisión diaria de dependencias</td></tr>
        </tbody>
      </table>
    </div>''',
    "Cuatro tipos que aparecen en las guías de 2026. El loop de meta, que itera hasta cumplir una condición verificable. El recurrente, que repite una tarea cada cierto tiempo. El de evaluador y optimizador: uno genera y otro critica. Fallo típico: los dos convergen en la misma respuesta equivocada, o el evaluador se vuelve más permisivo. Y el de monitoreo. Cuándo no usar un loop: si una sola llamada bien armada resuelve la tarea. Empieza simple.",
    steps=2)

# 20 GUARDRAILS + TERMINAL ---------------------------------------------------
gr = ["Topes de vueltas y costo","Salida verificable","Permisos mínimos","Humano en lo irreversible","Trazas"]
grh = "".join(f'''<div class="reveal r-left" data-step="3" style="display:flex;gap:20px;align-items:center;font-size:29px;color:#fff"><span style="font-family:var(--cs-font-mono);color:var(--scd-lime)">0{i+1}</span>{t}</div>''' for i,t in enumerate(gr))
add("Guardrails", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">04 · Loop engineering</div>
      <h2 class="title reveal r-rise" data-step="1">Un loop sin tope es una factura sin tope</h2>
      <div style="display:grid;grid-template-columns:1.05fr .95fr;gap:70px">
        <div class="term reveal r-blur" data-step="2">
          <div class="bar"><i></i><i></i><i></i><span>agente · ejemplo</span></div>
<pre><span class="p">/goal</span> tests de auth en verde · tope 3
<span class="dim">vuelta 1</span>  <span class="ko">4 tests fallan</span>
<span class="dim">vuelta 2</span>  <span class="ko">1 test falla</span>
<span class="dim">vuelta 3</span>  <span class="ko">1 test falla</span>
<span class="ok">Tope alcanzado: me detengo</span></pre>
        </div>
        <div class="stagger" style="display:flex;flex-direction:column;gap:26px;justify-content:center">{grh}</div>
      </div>
    </div>''',
    "Demo mínima de 3 minutos: un /goal con una meta verificable, por ejemplo que pasen los tests de un módulo, con tope de 3 iteraciones, y mostrar que se corta y por qué. La salida de la terminal es ilustrativa: ajustar a la sintaxis real del agente que use. Guardrails no negociables: topes, salida verificable por una máquina, sandbox y permisos mínimos porque todo lo que lee el agente es entrada no confiable, compuertas humanas antes de lo irreversible y trazas. En mi proyecto: trabajó mientras yo tomaba un café.",
    steps=3)

# 21 TRANSICION ORCA ------------------------------------------------------------
add("Transicion Orca", f'''
    {K("sorprendido","left:170px;bottom:150px;width:340px")}
    <div class="pad center">
      <div class="eyebrow">05 · Orquestación</div>
      <h1 class="ts-title" style="font-size:160px">De un agente a una <span class="grad-word">flota</span></h1>
      <div class="ts-tagline">Tú marcas el ritmo, cada agente toca su parte</div>
    </div>''',
    "Con un solo agente trabajas en secuencia y esperas mucho. Con una flota, coordinas: tú defines, los agentes ejecutan en paralelo y los humanos deciden en las compuertas. Es el nivel 4 de Shapiro. Analogía: dirigir una orquesta. Y sí, la herramienta se llama Orca, de orquesta (chiste suave). Ahora volvemos a los tres agentes del inicio.")

# 22 QUE ES ORCA --------------------------------------------------------------
feat = [("Paralelo","Varios agentes, un worktree cada uno"),("Revisión","Diffs anotados línea a línea"),("Móvil","Avisa cuando un agente termina"),("CLI","Un agente coordina a otros")]
fh = "".join(f'''<div class="reveal r-left" data-step="2" style="display:grid;grid-template-columns:200px 1fr;gap:20px;align-items:baseline"><div style="font-family:var(--cs-font-heading);font-size:40px;text-transform:uppercase;color:var(--scd-cyan)">{a}</div><div style="font-size:28px;color:#fff">{b}</div></div>''' for a,b in feat)
add("Que es Orca", f'''
    <div class="skew reveal r-blur" data-step="1" style="right:150px;top:200px;width:560px;height:400px"><img src="assets/img/robot.jpg" alt="Equipo trabajando en una mesa con documentos"></div>
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">05 · Orquestación</div>
      <h2 class="title reveal r-rise" data-step="1">Orca: dirige tu flota</h2>
      <div class="stagger" style="display:flex;flex-direction:column;gap:22px;max-width:1000px">{fh}</div>
      <div class="reveal r-rise" data-step="3" style="margin-top:44px;display:flex;gap:30px;align-items:center">
        <div class="term" style="flex:none"><pre style="padding:16px 26px;font-size:26px"><span class="p">$</span> brew install --cask stablyai/orca/orca</pre></div>
        <div class="chips"><span class="chip lime">Open source · MIT</span><span class="chip">Tus suscripciones</span></div>
      </div>
    </div>''',
    "Orca es un ADE, Agent Development Environment, open source de Stably AI, licencia MIT, para macOS, Windows y Linux, con app móvil. Corre Claude Code, Codex, OpenCode, Gemini y cualquier agente de CLI, cada uno en su propio git worktree. No revende cómputo: usas tus propias suscripciones. También tiene SSH, navegador integrado y flujos con GitHub y Linear.",
    steps=3)

# 23 APUESTA ------------------------------------------------------------------
ag = [("A","Claude Code","72"),("B","Codex","88"),("C","Gemini CLI","54")]
agh = "".join(f'''<div class="hud reveal r-rise" data-step="1" style="flex:1"><div style="display:flex;justify-content:space-between;align-items:center"><div class="ring">{l}</div><div class="tag">worktree-{l.lower()}</div></div><h3 style="margin-top:22px">{n}</h3><div style="height:12px;background:rgba(31,211,245,.15);margin-top:16px"><div style="height:100%;width:{p}%;background:linear-gradient(90deg,var(--scd-cyan),var(--scd-lime))"></div></div></div>''' for l,n,p in ag)
add("Apuesta del ganador", f'''
    {K("interactuando","right:150px;top:96px;width:330px")}
    <div class="pad">
      <div class="eyebrow">Demo en vivo</div>
      <h2 class="title">¿Qué agente gana?</h2>
      <div class="stagger" style="display:flex;gap:36px;margin-top:20px">{agh}</div>
      <div class="payoff reveal r-mask" data-step="2" style="margin-top:56px">Votamos, comparamos diffs, merge del mejor</div>
    </div>''',
    "Volvemos a los tres agentes que lancé al inicio. Momento de juego: la sala vota cuál va a ganar, A, B o C. Abro Orca, comparamos los diffs lado a lado y hacemos merge del mejor. Las barras de la diapositiva son ilustrativas: los nombres de los agentes se ajustan a los que se usen en vivo. Si algo falla, plan B: video grabado ayer.",
    steps=2)

# 24 DAG --------------------------------------------------------------------
def node(x,y,t,cl=""):
    return f'<div class="hud node{cl}" style="position:absolute;left:{x}px;top:{y}px;width:250px;padding:22px 26px;text-align:center"><h3 style="font-size:36px;margin:0">{t}</h3></div>'
add("Orquestacion real", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">05 · Orquestación</div>
      <h2 class="title reveal r-rise" data-step="1">No es solo paralelizar</h2>
      <div class="reveal r-fade" data-step="2" style="position:relative;height:340px;width:1620px">
        <svg viewBox="0 0 1620 340" style="position:absolute;inset:0" aria-hidden="true" fill="none" stroke="#1FD3F5" stroke-width="3" stroke-opacity=".7">
          <path d="M250 170 H330"/><path d="M580 170 C620 170 620 70 660 70"/><path d="M580 170 C620 170 620 270 660 270"/>
          <path d="M910 70 C950 70 950 170 990 170"/><path d="M910 270 C950 270 950 170 990 170"/><path d="M1240 170 H1320" stroke="#D2F21E"/>
        </svg>
        {node(0,125,"Modelo")}{node(330,125,"API")}{node(660,25,"UI")}{node(660,225,"Pruebas")}{node(990,125,"Compuerta","  red")}{node(1320,125,"Merge"," lime")}
      </div>
      <div class="chips reveal r-rise" data-step="3" style="margin-top:40px"><span class="chip">task-create</span><span class="chip">dispatch</span><span class="chip">ask · reply</span><span class="chip lime">gate-create</span><span class="chip">run</span></div>
    </div>''',
    "Orquestación de verdad: Orca trae una skill de orquestación. Defines el trabajo como un DAG de tareas con dependencias y estados; despachas cada tarea a un trabajador en una terminal; los trabajadores preguntan al coordinador y esperan respuesta; y las compuertas de decisión bloquean una tarea hasta que un humano la resuelve. Esto es loop engineering aplicado. Demo: disparo una compuerta y la respondo desde el teléfono con la app móvil. Antes de la charla: correr orca orchestration --help y confirmar si la versión usa run o run-create.",
    steps=3)

# 25 BALANCE ---------------------------------------------------------------
add("Orquestar no reemplaza revisar", f'''
    {K("cansado","right:150px;bottom:160px;width:340px")}
    <div class="pad" style="justify-content:center">
      <div class="quote" style="max-width:1300px">
        <blockquote>Paralelizar sin verificar solo multiplica la revisión</blockquote>
        <cite>Más agentes, más importa el harness</cite>
      </div>
    </div>''',
    "Punto de equilibrio: orquestar no reemplaza revisar. Cuantos más agentes en paralelo, más importa el harness y las compuertas humanas. Kori aquí representa a quien recibe cinco PRs de mil líneas un viernes. En mi proyecto: pasé de programar a dirigir, pero sigo decidiendo. Otras opciones de pasada: Claude Squad, Warp, Composio, Symphony.")

# 26 TU RUTA --------------------------------------------------------------
lvls = [("A","Usuario avanzado","AGENTS.md y un flujo plan, ejecutar, validar",""),("B","Constructor de harness","2 o 3 skills propias y un repo legible"," lime"),("C","Constructor de agentes","Un agente en producción con evaluaciones"," red")]
lh = "".join(f'''<div class="hud{cl} reveal r-rise" data-step="2" style="flex:1;min-height:420px"><div class="ring{cl}">{l}</div><h3 style="margin-top:26px">{t}</h3><div class="tag" style="margin:18px 0 10px">Entregable</div><p>{d}</p></div>''' for l,t,d,cl in lvls)
add("Tu ruta", f'''
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">06 · Tu ruta</div>
      <h2 class="title reveal r-rise" data-step="1">Tres niveles hacia constructor</h2>
      <div class="stagger" style="display:flex;gap:36px">{lh}</div>
    </div>''',
    "Ya tienes casi todo: los agentes son software y fallan como software. Lo nuevo es aceptar que la salida es probabilística y aprender a medirla. Nivel A: usuario avanzado. Nivel B: constructor de harness, diseñas el entorno donde trabajan los agentes de tu equipo. Nivel C: constructor de agentes como producto, con bucle, herramientas, memoria, evaluaciones y guardrails. Frameworks para elegir uno y construir: LangGraph, Claude Agent SDK, OpenAI Agents SDK.",
    steps=2)

# 27 90 DIAS --------------------------------------------------------------
add("Plan de 90 dias", f'''
    {K("entusiasta","right:150px;top:100px;width:280px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">06 · Tu ruta</div>
      <h2 class="title reveal r-rise" data-step="1">Tu plan de 90 días</h2>
      <ol class="sz-timeline stagger" style="margin-top:80px">
        <li class="reveal" data-step="2"><span class="when">Días 1 a 30</span><h3>Sube un nivel</h3><p>AGENTS.md y preguntas repetidas</p></li>
        <li class="reveal" data-step="2"><span class="when">Días 31 a 60</span><h3>Tu harness</h3><p>Skills, sensores, un /goal</p></li>
        <li class="reveal hl" data-step="2"><span class="when">Días 61 a 90</span><h3>Tu agente</h3><p>Pequeño, evaluado y publicado</p></li>
      </ol>
    </div>''',
    "Plan de 90 días. Primer mes: sube un nivel como usuario. Segundo mes: construye tu harness. Tercer mes: construye un agente pequeño y completo con un framework, con evaluaciones y trazas, y publícalo como repositorio, servidor MCP o artículo. Para estudiantes: lo que pusiste en producción vale más que las credenciales.",
    steps=2)

# 28 PLAN DEL LUNES --------------------------------------------------------
mon = [("01","Crea AGENTS.md en tu repo"),("02","Anota cada pregunta repetida"),("03","Prueba un /goal con tope")]
mh = "".join(f'''<div class="reveal r-left" data-step="2" style="display:flex;gap:34px;align-items:center"><div class="ring{' lime' if n=='03' else ''}" style="width:110px;height:110px;font-size:38px">{n}</div><div style="font-family:var(--cs-font-heading);font-size:60px;text-transform:uppercase;color:#fff">{t}</div></div>''' for n,t in mon)
add("Plan del lunes", f'''
    {K("determinado","right:150px;bottom:160px;width:340px")}
    <div class="pad">
      <div class="eyebrow reveal" data-step="1">Lo prometido</div>
      <h2 class="title reveal r-rise" data-step="1">Elige una para el lunes</h2>
      <div class="stagger" style="display:flex;flex-direction:column;gap:40px;margin-top:10px">{mh}</div>
    </div>''',
    "Lo prometido al inicio. Cada persona elige una de estas tres acciones y la dice en voz alta a quien tiene al lado, o la anota. Comprometerse en público sube la probabilidad de hacerlo.",
    steps=2)

# 29 CIERRE ----------------------------------------------------------------
add("Cierre", f'''
    {K("corazon","left:170px;bottom:150px;width:360px")}
    <div class="pad" style="justify-content:center;padding-left:640px">
      <div class="eyebrow">Gracias · Cochabamba</div>
      <h1 class="cover-md">Pasas de escribir código a diseñar el <span class="grad-word">sistema que lo escribe</span></h1>
      <div style="font-size:30px;line-height:1.6;color:var(--cs-body);margin-top:44px">Ubica tu nivel y sube uno<br>Escribe el entorno antes que el código<br>Diseña loops, orquesta, decide tú</div>
      <div class="mono" style="font-size:34px;color:var(--scd-cyan);margin-top:36px">IG @tokidev.ai · GitHub @tokidev-ai</div>
    </div>''',
    "Tres ideas para llevarse: ubica tu nivel y sube uno; escribe el entorno antes que el código; deja de dirigir cada turno, diseña loops y orquesta, con un humano en las compuertas. Me encuentran en Instagram @tokidev.ai y en GitHub @tokidev-ai. Gracias, y a preguntas.",
    cls="grad")
