def gardien(nb_marche,cm_marche):
    resulte = 0
    for i in range(6):
        resulte += nb_marche * cm_marche

    resulte_aller_retour = resulte * 2 

    resulte_semaine = resulte_aller_retour * 7

    resulte_m_semaine = resulte_semaine * 100

    print("Pour",nb_marche,"marches de", cm_marche, "cm, le gardien parcourt",resulte_m_semaine,"m par semaine.")


gardien(5,5)