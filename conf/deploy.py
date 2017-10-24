DIR_SRC = "/home/appadmin/hason"
BACKUP_DIR_TIME_FORMAT = "%Y%m%d-%H%M"

################# jar #################

JAR_DIR_DEST = "/usr/local/dubbox"
JAR_BACKUP_DIR = "/home/appadmin/dubbox_backup/{time}"

################# war #################

WAR_BACKUP_DIR = "/home/appadmin/tomcat_backup/{time}/tomcat_{dir_index}_backup"
WAR_DIR_DEST = "/usr/local/tomcat_{dir_index}/webapps"

################# common war #################

CWAR_DIR_MAP = {
    '0' : ['AccountWeb.war', 'UserWeb.war', 'ActivityWeb.war', 'FinancialWeb.war', 'MessageWeb.war'], 

    '1' : ['AssetWeb.war', 'ProductWeb.war', 'trustee.war', 'MarketWeb.war'],

    '2' : ['CMSWeb.war', 'MobileWeb.war', 'RewardWeb.war', 'WapWeb.war', 'RiskControlWeb.war'],

    '3' : ['MarketChannelCoopWeb.war'],

    'open_8084' : ['BusinessOpenWeb.war', 'OpenDataWeb.war']
}

################# admin war #################

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
SVN_CHECKOUT_DIR = "/srv/salt/svn_package"
SALT_SVN_PATH = "salt://svn_package"


################# ssh #################
SSH_PRIVATE_KEY_FILE = ""