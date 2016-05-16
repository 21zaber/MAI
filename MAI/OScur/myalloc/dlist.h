#pragma once

#define DL_FOREACH(head, el)                                                                   \
    for(el=head; el; el=(el)->next)

#define DL_FOREACH_SAFE(head, el, tmp)                                                         \
    for((el)=(head);(el) && (tmp = (el)->next, 1); (el) = tmp)
                                                                                          
#define DL_PREPEND(head, add)                                                                  \
do {                                                                                           \
 (add)->next = head;                                                                           \
 if (head) {                                                                                   \
   (add)->prev = (head)->prev;                                                                 \
   (head)->prev = (add);                                                                       \
 } else {                                                                                      \
   (add)->prev = (add);                                                                        \
 }                                                                                             \
 (head) = (add);                                                                               \
} while (0)

#define DL_APPEND(head, add)                                                                   \
do {                                                                                           \
  if (head) {                                                                                  \
      (add)->prev = (head)->prev;                                                              \
      (add)->next = NULL;                                                                      \
      (head)->prev->next = (add);                                                              \
      (head)->prev = (add);                                                                    \
  } else {                                                                                     \
      (add)->prev = (add);                                                                     \
      (add)->next = NULL;                                                                      \
      (head)=(add);                                                                            \
  }                                                                                            \
} while (0)

#define DL_CONCAT(head1, head2, tmp)                                                           \
do {                                                                                           \
  if (head2) {                                                                                 \
    if (head1) {                                                                               \
        tmp = (head2)->prev;                                                                   \
        (head2)->prev = (head1)->prev;                                                         \
        (head1)->prev->next = (head2);                                                         \
        (head1)->prev = tmp;                                                                   \
    } else {                                                                                   \
        (head1)=(head2);                                                                       \
    }                                                                                          \
  }                                                                                            \
} while (0)

#define DL_DELETE(head, del)                                                                   \
do {                                                                                           \
  assert((del)->prev != NULL);                                                                 \
  if ((del)->prev == (del)) {                                                                  \
      (head) = NULL;                                                                           \
  } else if ((del) == (head)) {                                                                \
      (del)->next->prev = (del)->prev;                                                         \
      (head) = (del)->next;                                                                    \
  } else {                                                                                     \
      (del)->prev->next = (del)->next;                                                         \
      if ((del)->next) {                                                                       \
          (del)->next->prev = (del)->prev;                                                     \
      } else {                                                                                 \
          (head)->prev = (del)->prev;                                                          \
      }                                                                                        \
  }                                                                                            \
} while (0)

#define DL_COUNT(head, el, counter)                                                            \
{                                                                                              \
    counter = 0;                                                                               \
    DL_FOREACH(head, el){ ++counter; }                                                         \
}
