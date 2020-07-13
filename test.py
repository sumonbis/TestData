for batch in range(total_batch):
            batch_x, batch_y = mnist.train.next_batch(batch_size)
            sess.run(train_op, feed_dict={x:batch_x, y:batch_y})

        if epoch % 10 == 0:
            loss_, acc = sess.run([loss, accuracy], feed_dict={x:batch_x, y:batch_y})
            print("epoch {},  loss {:.4f}, acc {:.3f}".format(epoch, loss_, acc))
