def arithmetic_arranger(problems, display_ans=False):
  arranged_problems=""
  if len(problems) > 5:
    return "Error: Too many problems."

  probs=[ p.split(" ") for p in problems ]
  ops=list(set([ p[1] for p in probs ]))
  for op in ops:
    if op not in ["-","+"]:
      return "Error: Operator must be '+' or '-'." 
  
  for p in probs:
    if not p[0].isnumeric() or not p[2].isnumeric():
      return "Error: Numbers must only contain digits."
      
    if len(p[0])>4 or len(p[2])>4:
        return "Error: Numbers cannot be more than four digits."
  
  ans=[ eval(p[0])-eval(p[2]) if p[1]=="-" else eval(p[0])+eval(p[2]) for p in probs]
  
  print (probs,"\n",ans)

  op1_str=""
  op2_str=""
  sep_str=""
  ans_str=""

  for i,(p_a) in enumerate(zip(probs,ans)):
    p=p_a[0]
    a=str(p_a[1])
    len_op1=len(p[0])
    len_op2=len(p[2])
    max_len=max(len_op1,len_op2)
    # max len + space + operator
    sep_len=max_len+2
    ans_len=len(a)
    op1_str+=" "*(2+(max_len-len_op1))+p[0]
    op2_str+=p[1]+" "*(1+(max_len-len_op2))+p[2]
    sep_str+="-"*sep_len
    ans_str+=" "*(2+(max_len-ans_len))+a
    

    if i<len(probs)-1:
      op1_str+=" "*4
      op2_str+=" "*4
      sep_str+=" "*4
      ans_str+=" "*4
    

  op1_str+="\n"
  op2_str+="\n"
  

  # print(op1_str, op2_str, sep_str, ans_str)
  arranged_problems=op1_str+op2_str+sep_str
  if display_ans:
    sep_str+="\n"
    arranged_problems=op1_str+op2_str+sep_str+ans_str
  print(arranged_problems)
  return arranged_problems

if __name__=="__main__":
  arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43'])
  # arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49'])