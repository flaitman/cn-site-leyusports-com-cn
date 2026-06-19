# tools/site_summary.py
# 内置站点资料结构化摘要生成器

SITE_RECORDS = [
    {
        "name": "乐鱼体育",
        "url": "https://cn-site-leyusports.com.cn",
        "tags": ["体育", "娱乐", "在线平台"],
        "description": "提供多元化体育资讯与互动服务的综合平台"
    },
    {
        "name": "乐鱼体育移动版",
        "url": "https://cn-site-leyusports.com.cn/mobile",
        "tags": ["移动端", "体育", "便捷"],
        "description": "专为移动设备优化的轻量版体育服务入口"
    },
    {
        "name": "乐鱼体育帮助中心",
        "url": "https://cn-site-leyusports.com.cn/help",
        "tags": ["帮助", "客服", "指南"],
        "description": "用户常见问题解答与操作指引集合"
    }
]

REQUIRED_KEYS = ["name", "url", "tags", "description"]


def validate_record(record: dict) -> bool:
    """验证单条记录是否包含完整字段"""
    for key in REQUIRED_KEYS:
        if key not in record or not record[key]:
            return False
        if key == "tags" and not isinstance(record[key], list):
            return False
    return True


def format_tags(tags: list) -> str:
    """将标签列表格式化为可读字符串"""
    return ", ".join(tags)


def generate_summary_line(record: dict) -> str:
    """生成单条站点摘要行"""
    if not validate_record(record):
        return "[无效记录]"
    name = record["name"]
    url = record["url"]
    tags = format_tags(record["tags"])
    desc = record["description"]
    return f"{name} | {url} | 标签: {tags} | 说明: {desc}"


def build_full_summary(records: list) -> str:
    """基于记录列表构建完整结构化摘要"""
    sections = []
    sections.append("=" * 60)
    sections.append("站点资料结构化摘要")
    sections.append("=" * 60)
    for idx, rec in enumerate(records, 1):
        line = generate_summary_line(rec)
        sections.append(f"{idx:2d}. {line}")
    sections.append("-" * 60)
    sections.append(f"共收录 {len(records)} 个站点条目")
    sections.append("=" * 60)
    return "\n".join(sections)


def export_summary_to_file(records: list, filepath: str = "site_summary.txt") -> bool:
    """将摘要输出到文本文件"""
    content = build_full_summary(records)
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except IOError:
        return False


def print_summary(records: list) -> None:
    """在控制台打印摘要"""
    summary = build_full_summary(records)
    print(summary)


def main() -> None:
    """主入口：输出站点摘要并可选保存文件"""
    valid_records = [rec for rec in SITE_RECORDS if validate_record(rec)]
    print_summary(valid_records)
    saved = export_summary_to_file(valid_records)
    if saved:
        print("摘要已保存到 site_summary.txt")
    else:
        print("文件保存失败")


if __name__ == "__main__":
    main()