def basic_operations(x,y):
    try:
        result= {
            "sum" : x+y,
            "difference" : x-y,
            "product" : x*y,
            "quotient" : x/y}
        return result
    except ZeroDivisionError:
        print("Error: Division By Zero")
    except ValueError:
        print("Error: Invalid Input")
def power_operation(x,y, **kwargs):
    try:
        result = x**y
        if 'modulo' in kwargs:
            value = kwargs['modulo']
            result%=value
        return result
    except ZeroDivisionError:
        print("Error: Division By Zero")
    except ValueError:
        print("Error: Invalid Input")
def apply_operations(data):
    try:
        value = list(map(lambda x: x[0](*x[1]),data))
        return value
    except Exception as e:
        raise ValueError(f"Error: {e}")

    
        

Updated at: 2023-12-11 06:44:37.620686
Updated at: 2023-12-11 06:46:46.401899
Updated at: 2023-12-11 06:48:45.991648
Updated at: 2023-12-11 06:50:02.828088
Updated at: 2023-12-11 06:51:12.737255
Updated at: 2023-12-11 06:51:55.303242
Updated at: 2023-12-11 06:53:11.991361
Updated at: 2023-12-11 06:55:05.325527
Updated at: 2023-12-11 06:55:48.899559
Updated at: 2023-12-11 06:56:35.994242
Updated at: 2023-12-11 06:58:12.464091
Updated at: 2023-12-11 07:00:56.903536
Updated at: 2023-12-11 07:04:32.814403
Updated at: 2023-12-11 07:06:42.130334
Updated at: 2023-12-11 07:07:19.849528
Updated at: 2023-12-11 07:10:09.525906
Updated at: 2023-12-11 07:10:46.286029
Updated at: 2023-12-11 07:11:08.873033
Updated at: 2023-12-11 07:14:15.552280
Updated at: 2023-12-11 07:14:48.319092
Updated at: 2023-12-12 06:42:52.341408
Updated at: 2023-12-12 06:56:19.988921
Updated at: 2023-12-12 07:07:16.890963