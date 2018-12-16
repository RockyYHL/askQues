from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from rest_framework.decorators import api_view
from wjdc.models import B_RT,B_XS,B_CR

@api_view(['POST'])
@csrf_exempt
def setToBase1(request):

    try:
        print(request.data)
        print("没出事")
        print(request.data["answer[PopulationID]"])

        B_RT.objects.update_or_create(PopulationID=request.data["answer[PopulationID]"],
                                                name =request.data["answer[name]"],
                                                checkYear = request.data["answer[checkYear]"],
                                                checkMonth = request.data["answer[checkMonth]"],
                                                checkDay = request.data["answer[checkDay]"],
                                                checherID = request.data["answer[checherID]"],
                                                B_RT_Q1 = request.data["answer[Q1]"],
                                                B_RT_Q2 = request.data["answer[Q2]"],
                                                B_RT_Q3 = request.data["answer[Q3]"],
                                                B_RT_Q4a = request.data["answer[Q4a]"],
                                                B_RT_Q4b = request.data["answer[Q4b]"],
                                                B_RT_Q4c = request.data["answer[Q4c]"],
                                                B_RT_Q5 = request.data["answer[Q5]"],
                                                B_RT_Q6 = request.data["answer[Q6]"],
                                                B_RT_Q7 = request.data["answer[Q7]"],
                                                B_RT_Q8 = request.data["answer[Q8]"],
                                                B_RT_Q9 = request.data["answer[Q9]"],
                                                B_RT_Q10 = request.data["answer[Q10]"],
                                                B_RT_Q11 = request.data["answer[Q11]"],
                                                B_RT_Q12 = request.data["answer[Q12]"],
                                                B_RT_Q13 = request.data["answer[Q13]"],
                                                B_RT_Q14 = request.data["answer[Q14]"],
                                                B_RT_Q15 = request.data["answer[Q15]"],
                                                B_RT_Q16 = request.data["answer[Q16]"],
                                                B_RT_Q17 = request.data["answer[Q17]"],
                                                B_RT_Q18 = request.data["answer[Q18]"],
                                                B_RT_Q19 = request.data["answer[Q19]"],
                                                B_RT_Q20 = request.data["answer[Q20]"],
                                                B_RT_Q21a = request.data["answer[Q21a]"],
                                                B_RT_Q21b=request.data["answer[Q21b]"],
                                                B_RT_Q21c=request.data["answer[Q21c]"],
                                                B_RT_Q21d=request.data["answer[Q21d]"],
                                                B_RT_Q21e=request.data["answer[Q21e]"],
                                                B_RT_Q21f=request.data["answer[Q21f]"],
                                                B_RT_Q22a = request.data["answer[Q22a]"],
                                                B_RT_Q22b=request.data["answer[Q22b]"],
                                                B_RT_Q22c=request.data["answer[Q22c]"],
                                                B_RT_Q22d=request.data["answer[Q22d]"],
                                                B_RT_Q22e=request.data["answer[Q22e]"],
                                                B_RT_Q22f=request.data["answer[Q22f]"],
                                                B_RT_Q22g=request.data["answer[Q22g]"],
                                                B_RT_Q22h=request.data["answer[Q22h]"],
                                                B_RT_Q23 = request.data["answer[Q23]"],
                                                B_RT_Q24 = request.data["answer[Q24]"],
                                                B_RT_Q25 = request.data["answer[Q25]"])

        body = {"status": 1, "msg": "数据录入数据库发生成功"}
        print(body)

    except:
        body={"status":0,"msg":"数据录入数据库发生异常"}
        print(body)

    return Response(body)


@api_view(['POST'])
@csrf_exempt
def setToBase2(request):

    try:
        print(request.data)
        print("没出事")
        print(request.data["answer[PopulationID]"])

        B_XS.objects.update_or_create(PopulationID=request.data["answer[PopulationID]"],
                                                name =request.data["answer[name]"],
                                                school = request.data["answer[school]"],
                                                grade=request.data["answer[grade]"],
                                                classes=request.data["answer[classes]"],
                                                checkYear=request.data["answer[checkYear]"],
                                                checkMonth = request.data["answer[checkMonth]"],
                                                checkDay = request.data["answer[checkDay]"],
                                                checherID = request.data["answer[checkerID]"],
                                                B_XS_Q1 = request.data["answer[Q1]"],
                                                B_XS_Q2 = request.data["answer[Q2]"],
                                                B_XS_Q3 = request.data["answer[Q3]"],
                                                B_XS_Q4 = request.data["answer[Q4]"],

                                                B_XS_Q5 = request.data["answer[Q5]"],
                                                B_XS_Q6 = request.data["answer[Q6]"],
                                                B_XS_Q7 = request.data["answer[Q7]"],
                                                B_XS_Q8 = request.data["answer[Q8]"],
                                                B_XS_Q9a = request.data["answer[Q9a]"],
                                                B_XS_Q9b=request.data["answer[Q9b]"],
                                                B_XS_Q9c=request.data["answer[Q9c]"],
                                                B_XS_Q10 = request.data["answer[Q10]"],
                                                B_XS_Q11 = request.data["answer[Q11]"],
                                                B_XS_Q12 = request.data["answer[Q12]"],
                                                B_XS_Q13 = request.data["answer[Q13]"],
                                                B_XS_Q14 = request.data["answer[Q14]"],
                                                B_XS_Q15 = request.data["answer[Q15]"],
                                                B_XS_Q16 = request.data["answer[Q16]"],
                                                B_XS_Q17 = request.data["answer[Q17]"],
                                                B_XS_Q18 = request.data["answer[Q18]"],
                                                B_XS_Q19a = request.data["answer[Q19a]"],
                                                B_XS_Q19b=request.data["answer[Q19b]"],
                                                B_XS_Q19c=request.data["answer[Q19c]"],
                                                B_XS_Q19d=request.data["answer[Q19d]"],
                                                B_XS_Q19e=request.data["answer[Q19e]"],
                                                B_XS_Q19f=request.data["answer[Q19f]"],
                                                B_XS_Q19g=request.data["answer[Q19g]"],
                                                B_XS_Q19h=request.data["answer[Q19h]"],
                                                B_XS_Q20a = request.data["answer[Q20a]"],
                                                B_XS_Q20b=request.data["answer[Q20b]"],
                                                B_XS_Q20c=request.data["answer[Q20c]"],
                                                B_XS_Q20d=request.data["answer[Q20d]"],
                                                B_XS_Q21a = request.data["answer[Q21a]"],
                                                B_XS_Q21b=request.data["answer[Q21b]"],
                                                B_XS_Q21c=request.data["answer[Q21c]"],
                                                B_XS_Q21d=request.data["answer[Q21d]"],
                                                B_XS_Q21e=request.data["answer[Q21e]"],
                                                B_XS_Q21f=request.data["answer[Q21f]"],
                                                B_XS_Q21g=request.data["answer[Q21g]"],
                                                B_XS_Q21h=request.data["answer[Q21h]"],
                                                B_XS_Q21i=request.data["answer[Q21i]"],
                                                B_XS_Q22 = request.data["answer[Q22]"])


        body = {"status": 1, "msg": "数据录入数据库发生成功"}
        print(body)

    except:
        body={"status":0,"msg":"数据录入数据库发生异常"}
        print(body)

    return Response(body)


@api_view(['POST'])
@csrf_exempt
def setToBase3(request):

    try:
        print(request.data)
        print("没出事")
        print(request.data["answer[PopulationID]"])

        B_CR.objects.update_or_create(PopulationID=request.data["answer[PopulationID]"],
                                                name =request.data["answer[name]"],
                                                checkYear=request.data["answer[checkYear]"],
                                                checkMonth = request.data["answer[checkMonth]"],
                                                checkDay = request.data["answer[checkDay]"],
                                                checherID = request.data["answer[checkerID]"],
                                                B_CR_Q1 = request.data["answer[Q1]"],
                                                B_CR_Q2a = request.data["answer[Q2a]"],
                                                B_CR_Q2b=request.data["answer[Q2b]"],
                                                B_CR_Q2c=request.data["answer[Q2c]"],
                                                B_CR_Q3 = request.data["answer[Q3]"],
                                                B_CR_Q4 = request.data["answer[Q4]"],

                                                B_CR_Q5 = request.data["answer[Q5]"],
                                                B_CR_Q6 = request.data["answer[Q6]"],
                                                B_CR_Q7a = request.data["answer[Q7a]"],
                                                B_CR_Q7b=request.data["answer[Q7b]"],
                                                B_CR_Q7c=request.data["answer[Q7c]"],
                                                B_CR_Q8 = request.data["answer[Q8]"],
                                                B_CR_Q9 = request.data["answer[Q9]"],

                                                B_CR_Q10 = request.data["answer[Q10]"],
                                                B_CR_Q11 = request.data["answer[Q11]"],
                                                B_CR_Q12 = request.data["answer[Q12]"],
                                                B_CR_Q13 = request.data["answer[Q13]"],
                                                B_CR_Q14 = request.data["answer[Q14]"],
                                                B_CR_Q15 = request.data["answer[Q15]"],
                                                B_CR_Q16 = request.data["answer[Q16]"],
                                                B_CR_Q17a = request.data["answer[Q17a]"],
                                                B_CR_Q17b=request.data["answer[Q17b]"],
                                                B_CR_Q17c=request.data["answer[Q17c]"],
                                                B_CR_Q17d=request.data["answer[Q17d]"],
                                                B_CR_Q17e=request.data["answer[Q17e]"],
                                                B_CR_Q18 = request.data["answer[Q18]"],
                                                B_CR_Q19 = request.data["answer[Q19]"],

                                                B_CR_Q20a = request.data["answer[Q20a]"],
                                                B_CR_Q20b=request.data["answer[Q20b]"],
                                                B_CR_Q20c=request.data["answer[Q20c]"],
                                                B_CR_Q20d=request.data["answer[Q20d]"],
                                                B_CR_Q20e=request.data["answer[Q20e]"],
                                                B_CR_Q20f=request.data["answer[Q20f]"],
                                                B_CR_Q20g=request.data["answer[Q20g]"],
                                                B_CR_Q20h=request.data["answer[Q20h]"],
                                                B_CR_Q20i=request.data["answer[Q20i]"],
                                                B_CR_Q20j=request.data["answer[Q20j]"],
                                                B_CR_Q20k=request.data["answer[Q20k]"],
                                                B_CR_Q20l=request.data["answer[Q20l]"],
                                                B_CR_Q21= request.data["answer[Q21]"],

                                                B_CR_Q22 = request.data["answer[Q22]"],
                                                B_CR_Q23a=request.data["answer[Q23a]"],
                                                B_CR_Q23b=request.data["answer[Q23b]"],
                                                B_CR_Q23c=request.data["answer[Q23c]"],
                                                B_CR_Q23d=request.data["answer[Q23d]"],

                                                B_CR_Q24a=request.data["answer[Q24a]"],
                                                B_CR_Q24b=request.data["answer[Q24b]"],
                                                B_CR_Q24c=request.data["answer[Q24c]"],
                                                B_CR_Q24d=request.data["answer[Q24d]"],
                                                B_CR_Q24e=request.data["answer[Q24e]"],
                                                B_CR_Q24f=request.data["answer[Q24f]"],
                                                B_CR_Q24g=request.data["answer[Q24g]"],
                                                B_CR_Q24h=request.data["answer[Q24h]"],

                                                B_CR_Q25=request.data["answer[Q25]"],
                                                B_CR_Q25_6=request.data["answer[Q25_6]"],
                                                B_CR_Q26=request.data["answer[Q26]"],
                                                B_CR_Q27=request.data["answer[Q27]"],
                                      )


        body = {"status": 1, "msg": "数据录入数据库发生成功"}
        print(body)

    except:
        body={"status":0,"msg":"数据录入数据库发生异常"}
        print(body)

    return Response(body)
