import urllib.parse

template = """<div class="file-item">
            <a href="Mini%20test%20sylabus.pdf" class="file-item-name">
            <div class="file-item-select-bg bg-primary"></div>
            <div class="file-item-icon far fa-file-pdf text-secondary"></div>
                Mini test sylabus.pdf
            </a>
            <div class="file-item-actions btn-group">
                <button type="button" class="btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle" data-toggle="dropdown"><i class="ion ion-ios-more"></i></button>
                <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href="Mini%20test%20sylabus.pdf" download>Download</a>
                </div>
            </div>
        </div>"""
content = ["Additional Sciences.pdf","Ancient Medieval and Culture.pdf","Answer Writing Session Class.pdf","Biology.pdf","Disaster Management.pdf","Economics PG.pdf","Economics.pdf","Environment.pdf","Ethics Case Study.pdf","Ethics JG.pdf","Geography.pdf","Governance.pdf","How to Read Newspaper Class.pdf","International Relations.pdf","Introduction.pdf","Map.pdf","Modern Indian History.pdf","Polity.pdf","Post Independence India.pdf","Recorded Ethics JG.pdf","Recorded Ethics.pdf","Recorded Post Independence.pdf","Recorded Social Issues.pdf","Recorded Society.pdf","Science and Technology.pdf","Security.pdf","World History.pdf"]

for c in content:
    print("""        <div class="file-item">
            <a href=\"""" + urllib.parse.quote(c) + """" class="file-item-name">
            <div class="file-item-select-bg bg-primary"></div>
            <div class="file-item-icon far fa-file-pdf text-secondary"></div>
                """ + c + """
            </a>
            <div class="file-item-actions btn-group">
                <button type="button" class="btn btn-default btn-sm rounded-pill icon-btn borderless md-btn-flat hide-arrow dropdown-toggle" data-toggle="dropdown"><i class="ion ion-ios-more"></i></button>
                <div class="dropdown-menu dropdown-menu-right">
                    <a class="dropdown-item" href=\"""" + urllib.parse.quote(c) + """" download>Download</a>
                </div>
            </div>
        </div>""")