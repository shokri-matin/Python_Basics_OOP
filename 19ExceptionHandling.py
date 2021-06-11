
try:
    a = 1/0
except UnicodeDecodeError:
    print('UnicodeDecodeError')

except (TypeError, ZeroDivisionError):
    print('TypeError, ZeroDivisionError')

except:
    print('Some error is occurred!')

finally:
    print('This section will always run!')
