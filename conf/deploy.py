DIR_SRC = "/home/appadmin/hason"
BACKUP_DIR_TIME_FORMAT = "%Y%m%d-%H%M"

################# jar #################

JAR_DIR_DEST = "/usr/local/dubbox"
JAR_BACKUP_DIR_PREFIX = "/home/appadmin/dubbox_backup"

################# war #################
CWAR_BACKUP_DIR_PREFIX = "/home/appadmin/tomcat_backup"
CWAR_DIR_DEST = ["/usr/local/tomcat_{}/webapps".format(i) for i in range(0, 6)]
AWAR_DIR_MAP = {
    '0' : [], 

    '1' : [],

    '2' : [],

    '3' : [],

    '4' : [],

    '5' : []
}

################# admin war #################

AWAR_BACKUP_DIR_PREFIX = "/home/appadmin/tomcat_backup"
AWAR_DIR_DEST = ["/usr/local/tomcat_0/webapps", "/usr/local/tomcat_1/webapps"]
AWAR_DIR_MAP = {
    '0' : ['AccountAdminWeb.war', 
            'AdminWeb.war', 
            'AssetAdminWeb.war', 
            'ProductAdminWeb.war', 
            'TrusteeAdminWeb.war', 
            'UserAdminWeb.war', 
            'BusinessOpenAdminWeb.war', 
            'VisualDataAdminWeb.war'], 

    '1' : ['FinancialAdminWeb.war', 
            'AdminZookeeperWeb.war', 
            'CMSAdminWeb.war', 
            'MessageAdminWeb.war', 
            'MobileAdminWeb.war', 
            'RewardAdminWeb.war', 
            'MarketAdminWeb.war', 
            'RiskControlAdminWeb.war', 
            'FinanicialAdminWeb.war']
}





# FILES_PREFIX = [ "AccountApp",
#                  "ActivityApp",
#                  "ActivitySchedule",
#                  "AdminApp",
#                  "AssetApp",
#                  "AssetSchedule",
#                  "BusinessOpenApp",
#                  "BusinessOpenSchedule",
#                  "CMSApp",
#                  "CMSSchedule",
#                  "DataCollectSchedule",
#                  "DataFactoryApp",
#                  "FinancialApp",
#                  "FinancialPlanApp",
#                  "FinancialPlanSchdule",
#                  "IDApp",
#                  "MarketApp",
#                  "MarketSchedule",
#                  "MessageApp",
#                  "MessageSchedule",
#                  "ProductApp",
#                  "ProductSchedule",
#                  "RewardApp",
#                  "RewardSchedule",
#                  "RiskControlApp",
#                  "TrusteeApp",
#                  "TrusteeSchedule",
#                  "UserApp",
#                  "UserSchedule", ]


################# svn #################
SVN_USERNAME = "feng.huajiang"
SVN_PASSWORD = "huajiang@zyxr.com"
SVN_CHECKOUT_DIR = "/tmp/svn_package"


################# ssh #################
SSH_PRIVATE_KEY_FILE = ""