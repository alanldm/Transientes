def t_l(zl, z0):
    return (zl-z0)/(zl+z0)

def t_s(zs, z0):
    return (zs-z0)/(zs+z0)
    
def v_0(vs, z0, zs):
    return (z0*vs)/(z0+zs)

def v_l(vs, z0, zl):
    return (zl*vs)/(zl+z0)

def time(l, up):
    return l/up