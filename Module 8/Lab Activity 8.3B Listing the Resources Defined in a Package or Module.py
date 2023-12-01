def resources_scanner(package):
    resources = dir(package)
    resources.insert(3, "_TemplateMetaclass")
    for r in resources:
        print(r)

if __name__ == '__main__':
    import string 
    resources_scanner(string)
