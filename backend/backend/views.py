from django.http import JsonResponse


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_view(request, number):
    if request.method == 'GET':
        result = fibonacci(int(number))
        return JsonResponse({'number': number, 'fibonacci': result})
