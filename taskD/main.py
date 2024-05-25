import sys


class LogMobileDistinguisher:
    def __init__(self, desktop_agents, mobile_agents):
        self.desktop = self.create_agent_set(desktop_agents)
        self.mobile = self.create_agent_set(mobile_agents)
        self.process_log()

    @staticmethod
    def create_agent_set(file_name):
        with open(file_name, 'r') as f:
            return {line.strip() for line in f}

    def get_line_client(self, line_ua):
        if line_ua in self.desktop:
            return 'desktop'
        elif line_ua in self.mobile:
            return 'mobile'
        else:
            return 'unknown'

    @staticmethod
    def get_line_fields(line):
        result = []
        in_string = False
        s = ''
        for field in line.strip().split(' '):
            if not in_string:
                if field.startswith('"') and not field.endswith('"'):
                    in_string = True
                    s = field[1:]
                else:
                    result.append(field)
            else:
                if field.endswith('"'):
                    s += ' ' + field[:-1]
                    result.append(s)
                    in_string = False
                else:
                    s += ' ' + field
        return result

    def process_log(self):
        for line in sys.stdin:
            fields = self.get_line_fields(line)
            client = self.get_line_client(fields[6])
            print(client)

if __name__ == '__main__':
    LogMobileDistinguisher('d.txt', 'm.txt')
