from enums import ReportAdminStatus


def get_admin_status_dict() -> dict:
    return {ReportAdminStatus.NOT_HIRING: "Никем не взята в работу⚠",
            ReportAdminStatus.IN_WORK: "Взята в работу🔄",
            ReportAdminStatus.RESOLVED: "Проблема решена✅",
            ReportAdminStatus.REJECT:  "Жалоба отклонена❌"}
