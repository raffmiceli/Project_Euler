program Euler_31

  integer t, tr, steps, s, ch
  
  t = 0
  tr = 8
  s = 0
  
  steps = 200*100*40*20*10*4*2
  ch = steps/100
  
  do a = 0, 199
    do b = 0, 99
      do c = 0, 39
        do d = 0, 19
          do e = 0, 9
            do f = 0, 3
              do g = 0, 1
                t = a*1+b*2+c*5+d*10+e*20+f*50+g*100
                if (t == 200) then 
                  tr = tr+1
                end if
                s = s+1
                if (modulo(s,ch) == 0) then
                  write(6,*) s/ch,"% complete"
                end if
              end do
            end do
          end do
        end do
      end do
    end do
  end do  
                
  write(6,*) tr,s

end program Euler_31