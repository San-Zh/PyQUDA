from typing import List, NamedTuple


class RHMCParam(NamedTuple):
    norm_molecular_dynamics: float = 0.0
    residue_molecular_dynamics: List[float] = [1.0]
    offset_molecular_dynamics: List[float] = [0.0]
    norm_pseudo_fermion: float = 0.0
    residue_pseudo_fermion: List[float] = [1.0]
    offset_pseudo_fermion: List[float] = [0.0]
    norm_fermion_action: float = 0.0
    residue_fermion_action: List[float] = [1.0]
    offset_fermion_action: List[float] = [0.0]


clover_wilson = {
    2: RHMCParam(
        residue_molecular_dynamics=[
            1.0,
        ],
        offset_molecular_dynamics=[
            0.0,
        ],
        norm_pseudo_fermion=0.0,
        residue_pseudo_fermion=[
            1.0,
        ],
        offset_pseudo_fermion=[
            0.0,
        ],
    ),
    1: RHMCParam(
        residue_molecular_dynamics=[
            0.00943108618345698,
            0.0122499930158508,
            0.0187308029056777,
            0.0308130330025528,
            0.0521206555919226,
            0.0890870585774984,
            0.153090120000215,
            0.26493803350899,
            0.466760251501358,
            0.866223656646014,
            1.8819154073627,
            6.96033769739192,
        ],
        offset_molecular_dynamics=[
            5.23045292201785e-05,
            0.000569214182255549,
            0.00226724207135389,
            0.00732861083302471,
            0.0222608882919378,
            0.0662886891030569,
            0.196319420401789,
            0.582378159903323,
            1.74664271771668,
            5.42569216297222,
            18.850085313508,
            99.6213166072174,
        ],
        norm_pseudo_fermion=6.10610118771501,
        residue_pseudo_fermion=[
            -5.90262826538435e-06,
            -2.63363387226834e-05,
            -8.62160355606352e-05,
            -0.000263984258286453,
            -0.000792810319715722,
            -0.00236581977385576,
            -0.00704746125114149,
            -0.0210131715847004,
            -0.0629242233443976,
            -0.190538104129215,
            -0.592816342814611,
            -1.96992441194278,
            -7.70705574740274,
            -46.55440910469,
            -1281.70053339288,
        ],
        offset_pseudo_fermion=[
            0.000109335909283339,
            0.000584211769074023,
            0.00181216713967916,
            0.00478464392272826,
            0.0119020708754186,
            0.0289155646996088,
            0.0695922442548162,
            0.166959610676697,
            0.400720136243831,
            0.965951931276981,
            2.35629923417205,
            5.92110728201649,
            16.0486180482883,
            53.7484938194392,
            402.99686403222,
        ],
    ),
}

hisq = {
    0.500: RHMCParam(
        norm_molecular_dynamics=1.3325011583706989e-01,
        residue_molecular_dynamics=[
            1.2669186056995732e-01,
            2.7378920166284243e-01,
            5.5644974578431738e-01,
            1.1865868336039220e00,
            2.7858758337966751e00,
            8.3158629779846862e00,
            5.3208853108759094e01,
        ],
        offset_molecular_dynamics=[
            1.0996250034766824e00,
            1.7746229220144820e00,
            3.7756006003660438e00,
            9.3414743860895957e00,
            2.5702192260694158e01,
            8.3642288108773357e01,
            4.6252616250061345e02,
        ],
        norm_pseudo_fermion=2.8919739467122496e00,
        residue_pseudo_fermion=[
            -2.3557845961480885e-02,
            -8.2885482286405326e-02,
            -2.1764644603751068e-01,
            -5.4479339852426578e-01,
            -1.3860680088812929e00,
            -3.7765935660639274e00,
            -1.2139134088997151e01,
            -5.8588994817562380e01,
            -1.0307790286845684e03,
        ],
        offset_pseudo_fermion=[
            1.1040557735606693e00,
            1.5736800437416782e00,
            2.7153853579224934e00,
            5.2775876670360722e00,
            1.1058396002583724e01,
            2.4733869901006777e01,
            6.0995784602031200e01,
            1.8772293711130985e02,
            1.2192272712884435e03,
        ],
        norm_fermion_action=3.4578458119819977e-01,
        residue_fermion_action=[
            3.5964179588188865e-02,
            8.7012555774795899e-02,
            1.7462541549477295e-01,
            3.4715574154454032e-01,
            7.0939528613321157e-01,
            1.5416834731507183e00,
            3.8299173393357995e00,
            1.3040678914547950e01,
            1.1265862119439132e02,
        ],
        offset_fermion_action=[
            1.0746987053604169e00,
            1.4873530879912891e00,
            2.5167732300465526e00,
            4.8341829789898663e00,
            1.0047168154507411e01,
            2.2273672706059052e01,
            5.4049304390828183e01,
            1.5962500533655722e02,
            8.7553100280824765e02,
        ],
    ),
    0.050: RHMCParam(
        norm_molecular_dynamics=2.6567771557480493e-02,
        residue_molecular_dynamics=[
            5.4415326175599146e-02,
            9.0370308484060427e-02,
            1.8616389644513945e-01,
            4.0655052893921434e-01,
            9.1332229681707799e-01,
            2.2297215526003842e00,
            8.2673806076260998e00,
        ],
        offset_molecular_dynamics=[
            1.1651276172701218e-02,
            3.2128005558694356e-02,
            1.3618256552525199e-01,
            6.4581932161561295e-01,
            3.1710061679824459e00,
            1.6529546460530057e01,
            1.1696719959399913e02,
        ],
        norm_pseudo_fermion=6.6008968113477318e00,
        residue_pseudo_fermion=[
            -4.5244529588728673e-04,
            -2.7913286193527722e-03,
            -1.3910919905953502e-02,
            -6.7151227080820358e-02,
            -3.2392713062715339e-01,
            -1.5980690060213258e00,
            -8.5910485755168793e00,
            -6.3332591104281043e01,
            -1.8771881382968977e03,
        ],
        offset_pseudo_fermion=[
            1.3387699397698993e-02,
            3.1462323899226492e-02,
            9.6415385897133263e-02,
            3.2374992445020234e-01,
            1.1208318145761189e00,
            3.9545250804438625e00,
            1.4540181635176147e01,
            6.1963910644237338e01,
            5.3566592269333353e02,
        ],
        norm_fermion_action=1.5149456635663205e-01,
        residue_fermion_action=[
            6.0458038124269137e-03,
            1.5247824256426594e-02,
            3.7602970968999533e-02,
            9.4912662473817022e-02,
            2.4258769955049089e-01,
            6.3038339460769466e-01,
            1.7214395396814584e00,
            5.5998391201760676e00,
            3.6431278685560251e01,
        ],
        offset_fermion_action=[
            1.1680369733380888e-02,
            2.4528542115263768e-02,
            7.1946920045447768e-02,
            2.3818970133124504e-01,
            8.2029368099576661e-01,
            2.8788453123211895e00,
            1.0425969224178980e01,
            4.1948608522841752e01,
            2.6570653748247554e02,
        ],
    ),
}
