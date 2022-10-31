"""Log scripts."""
import logging
import time

from redis import from_url

client = from_url('redis://localhost:6379/1')

SEVERITY = {
    logging.DEBUG: 'debug',
    logging.INFO: 'info',
    logging.WARNING: 'warning',
    logging.ERROR: 'error',
    logging.CRITICAL: 'critical',
}

SEVERITY.update({(name, name) for name in SEVERITY.values()})

print(SEVERITY.get(logging.INFO))


def log_recent(name, message, severity=logging.INFO, pipe=None):
    # 尝试将日志的安全级别转换为简单的字符串
    severity = str(SEVERITY.get(severity)).lower()
    # 创建负责存储消息的键
    destination = f'recent:{name}:{severity}'
    # 将当前时间添加到消息里面，用于记录消息的发送时间
    message = time.asctime() + ' ' + message
    # 使用流水线将通信往返次数降低为一次
    pipe = pipe or client.pipeline()
    # 将消息添加到日志列表的最前面
    pipe.lpush(destination, message)
    # 对日志列表进行修剪，只包含最新的100条消息
    pipe.ltrim(destination, 0, 99)
    # 执行
    pipe.execute()

# def log_common(name, message,severity=logging.INFO)
